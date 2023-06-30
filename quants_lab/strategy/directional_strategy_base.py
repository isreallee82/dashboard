from datetime import datetime
from typing import Optional
import optuna


class DirectionalStrategyBase:

    def get_data(self, start: Optional[str] = None, end: Optional[str] = None):
        df = self.get_raw_data()
        return self.filter_df_by_time(df, start, end)

    def get_raw_data(self):
        raise NotImplemented

    def add_indicators(self, df):
        raise NotImplemented

    def add_signals(self, df):
        raise NotImplemented

    @staticmethod
    def filter_df_by_time(df, start: Optional[str] = None, end: Optional[str] = None):
        if start is not None:
            start_condition = df["timestamp"] >= datetime.strptime(start, "%Y-%m-%d")
        else:
            start_condition = True
        if end is not None:
            end_condition = df["timestamp"] <= datetime.strptime(end, "%Y-%m-%d")
        else:
            end_condition = True
        return df.loc[start_condition & end_condition]

    @staticmethod
    def optimize(study_name, objective, n_trials=1000):
        study = optuna.create_study(direction="maximize",
                                    study_name=study_name,
                                    storage="sqlite:///backtesting_report.db",
                                    load_if_exists=True)

        study.optimize(objective, n_trials=n_trials)
