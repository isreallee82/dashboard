from decimal import Decimal
import streamlit as st


def get_market_making_general_inputs_v1(custom_candles=False):
    with st.expander("General Settings", expanded=True):
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, \
            c13, c14, c15, c16, c17, c18, c19, c20, c21, c22 = st.columns(22)
        default_config = st.session_state.get("default_config", {})
        connector_name = default_config.get("connector_name", "kucoin")
        trading_pair = default_config.get("trading_pair", "WLD-USDT")
        leverage = default_config.get("leverage", 20)

        order_amount = default_config.get("order_amount", "")
        order_refresh_time = default_config.get("order_refresh_time", "")
        max_order_age = default_config.get("max_order_age", "")
        bid_spread = default_config.get("bid_spread", "") / Decimal('100')
        ask_spread = default_config.get("ask_spread", "") / Decimal('100')
        minimum_spread = default_config.get(
            "minimum_spread", "") / Decimal('100')
        order_levels = default_config.get("order_levels", "")
        # order_level_amount = default_config.get("order_level_amount", "")
        order_level_spread = default_config.get(
            "order_level_spread", "") / Decimal('100')
        inventory_skew_enabled = default_config.get(
            "inventory_skew_enabled", "")

        price_source = default_config.get("price_source", "")
        price_type = default_config.get("price_type", "")
        price_source_exchange = default_config.get("price_source_exchange", "")
        price_source_market = default_config.get("price_source_market", "")
        price_source_custom_api = default_config.get(
            "price_source_custom_api", "")
        custom_api_update_interval = default_config.get(
            "custom_api_update_interval", "")
        total_amount_quote = default_config.get("total_amount_quote", 1000)
        position_mode = 0 if default_config.get(
            "position_mode", "HEDGE") == "HEDGE" else 1
        cooldown_time = default_config.get("cooldown_time", 60 * 60) / 60
        executor_refresh_time = default_config.get(
            "executor_refresh_time", 60 * 60) / 60
        candles_connector = None
        candles_trading_pair = None
        interval = None
        with c1:
            connector_name = st.text_input("Connector", value=connector_name,
                                           help="Enter the name of the exchange to trade on (e.g., binance_perpetual).")
        with c2:
            trading_pair = st.text_input("Trading Pair", value=trading_pair,
                                         help="Enter the trading pair to trade on (e.g., WLD-USDT).")
        with c3:
            leverage = st.number_input("Leverage", value=leverage,
                                       help="Set the leverage to use for trading (e.g., 20 for 20x leverage). "
                                            "Set it to 1 for spot trading.")
        with c4:
            total_amount_quote = st.number_input("Total amount of quote", value=total_amount_quote,
                                                 help="Enter the total amount in quote asset to use for "
                                                      "trading (e.g., 1000).")
        with c5:
            position_mode = st.selectbox("Position Mode", ("HEDGE", "ONEWAY"), index=position_mode,
                                         help="Enter the position mode (HEDGE/ONEWAY).")
        with c6:
            cooldown_time = st.number_input("Stop Loss Cooldown Time (minutes)", value=cooldown_time,
                                            help="Specify the cooldown time in minutes after having a"
                                                 "stop loss (e.g., 60).") * 60
        with c7:
            executor_refresh_time = st.number_input("Executor Refresh Time (minutes)", value=executor_refresh_time,
                                                    help="Enter the refresh time in minutes for executors (e.g., 60).") * 60

        with c8:
            inventory_skew_enabled = st.text_input("inventory_skew_enabled" ("True", "False"), index=inventory_skew_enabled,
                                                   help="Would you like to enable inventory skew? (Yes/No) >>> ")
        with c9:
            bid_spread = st.number_input("bid_spread", value=bid_spread,
                                         help="How far away from the mid price do you want to place the "
                                         "first bid order? (Enter 1 to indicate 1%) >>> ")
        with c10:
            ask_spread = st.number_input("ask_spread", value=ask_spread,
                                         help="How far away from the mid price do you want to place the "
                                         "first ask order? (Enter 1 to indicate 1%) >>> ")
        with c11:
            order_refresh_time = st.selectbox("Order Refresh Time (minutes)", value=order_refresh_time,
                                              help="Enter the refresh time in minutes for order (e.g., 60).") * 60
        with c11:
            max_order_age = st.selectbox("Max Order Age (minutes)", value=max_order_age,
                                         help="How long do you want to cancel and replace bids and asks "
                                         "with the same price (in seconds)? >>> (e.g., 60).") * 60
        with c12:
            minimum_spread = st.number_input("Minimum spread", value=minimum_spread,
                                             help="At what minimum spread should the bot automatically "
                                             "cancel orders? (Enter 1 for 1%) >>> ") * 60
        with c13:
            order_amount = st.text_input("order_amount", value=order_amount,
                                         help="Ender Order amount")
        with c14:
            price_type = st.number_input("price_type", ("mid_price", "last_price", "last_own_trade_price", "best_bid", "best_ask", "inventory_cost"), index=price_type,
                                         help="Which price type to use? ("
                                         "mid_price/last_price/last_own_trade_price/best_bid/best_ask/inventory_cost) >>> ")
        with c15:
            price_source_exchange = st.number_input("price_source_exchange", value=price_source_exchange,
                                                    help="Enter external price source exchange name >>> ")
        with c16:
            order_levels = st.selectbox("order_levels", value=order_levels,
                                        help="How many orders do you want to place on both sides? >>> ")
        with c17:
            order_level_spread = st.number_input("order_level_spread", value=order_level_spread,
                                                 help="Enter the refresh time in minutes for executors (e.g., 60).") * 60
        with c18:
            price_source = st.text_input("Price Source", value=price_source,
                                         help="Enter the name of the exchange to trade on (e.g., binance_perpetual).")
        with c19:
            price_source_market = st.number_input("price source market", value=price_source_market,
                                                  help="Enter Price source market")
        with c20:
            price_source_custom_api = st.text_input("Price Source Custom Api", value=price_source_custom_api,
                                                    help="Enter pricing API URL >>> ")

        with c21:
            custom_api_update_interval = st.text_input("custom api update interval", value=custom_api_update_interval,
                                                       help="Enter custom API update interval in second (default: 5.0, min: 0.5) >>> ")
        with c22:
            strategy = st.text_input("Strategy", value=default_config.get("strategy", "simple_market_making"),
                                     help="Enter the strategy to use (e.g., simple_market_making).")
        if custom_candles:
            candles_connector = default_config.get(
                "candles_connector", "kucoin")
            candles_trading_pair = default_config.get(
                "candles_trading_pair", "WLD-USDT")
            interval = default_config.get("interval", "3m")
            intervals = ["1m", "3m", "5m", "15m", "1h", "4h", "1d"]
            interval_index = intervals.index(interval)
            with c1:
                candles_connector = st.text_input("Candles Connector", value=candles_connector,
                                                  help="Enter the name of the exchange to get candles from"
                                                       "(e.g., binance_perpetual).")
            with c2:
                candles_trading_pair = st.text_input("Candles Trading Pair", value=candles_trading_pair,
                                                     help="Enter the trading pair to get candles for (e.g., WLD-USDT).")
            with c3:
                interval = st.selectbox("Candles Interval", intervals, index=interval_index,
                                        help="Enter the interval for candles (e.g., 1m).")
    return connector_name, trading_pair, leverage, total_amount_quote, position_mode, cooldown_time, \
        executor_refresh_time, strategy, inventory_skew_enabled, bid_spread, ask_spread, order_refresh_time, max_order_age, \
        order_amount, price_type, price_source_exchange, order_levels, order_level_spread
