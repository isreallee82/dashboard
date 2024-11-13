from frontend.components.executors_distribution import get_executors_distribution_inputs
from frontend.components.market_making_general_inputs_v1 import get_market_making_general_inputs_v1
from frontend.components.risk_management import get_risk_management_inputs


def user_inputs():
    connector_name, trading_pair, leverage, total_amount_quote, position_mode, cooldown_time, \
        executor_refresh_time, strategy, inventory_skew_enabled, bid_spread, ask_spread, order_refresh_time, max_order_age, \
        order_amount, price_type, price_source_exchange, order_levels, order_level_spread, \
        _, _, _ = get_market_making_general_inputs_v1()
    buy_spread_distributions, sell_spread_distributions, buy_order_amounts_pct, \
        sell_order_amounts_pct = get_executors_distribution_inputs()
    sl, tp, time_limit, ts_ap, ts_delta, take_profit_order_type = get_risk_management_inputs()
    # Create the config
    config = {
        "controller_name": "simple_pmm",
        "controller_type": "market_making",
        "manual_kill_switch": None,
        "candles_config": [],
        "connector_name": connector_name,
        "trading_pair": trading_pair,
        "strategy": strategy,
        "bid_spread": bid_spread,
        "ask_spread": ask_spread,
        "order_refresh_time": order_refresh_time,
        "max_order_age": max_order_age,
        "order_amount": order_amount,
        "price_type": price_type,
        "price_source_exchange": price_source_exchange,
        "order_levels": order_levels,
        "order_level_spread": order_level_spread,
        "total_amount_quote": total_amount_quote,
        "buy_spreads": buy_spread_distributions,
        "sell_spreads": sell_spread_distributions,
        "buy_amounts_pct": buy_order_amounts_pct,
        "sell_amounts_pct": sell_order_amounts_pct,
        "executor_refresh_time": executor_refresh_time,
        "inventory_skew_enabled": inventory_skew_enabled,
        "cooldown_time": cooldown_time,
        "leverage": leverage,
        "position_mode": position_mode,
        "stop_loss": sl,
        "take_profit": tp,
        "time_limit": time_limit,
        "take_profit_order_type": take_profit_order_type.value,
        "trailing_stop": {
            "activation_price": ts_ap,
            "trailing_delta": ts_delta
        }
    }
    return config
