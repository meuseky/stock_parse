from datetime import datetime, timedelta

from src.lib.decorator import handle_zero_division

trade_date_format = "%d-%m-%Y %H:%M:%S"


class Trade(object):
    """
    Represents a single stock trade transaction
    """

    def __init__(self, symbol: str, price: float, volume: int,
                 trade_type: str, trade_date: str,
                 date_format: str=trade_date_format):
        """
        :param symbol: Stock symbol
        :param price:
        :param volume: Amount of shares
        :param trade_type: "buy" or "sell"
        :param trade_date:
        :return:
        """
        self.symbol = symbol
        self.price = price
        self.volume = volume
        self.trade_type = trade_type
        self.trade_date = datetime.strptime(trade_date, date_format)


class TradeList(object):
    """
    Contains a list of trade transactions, along with helper methods
    to process the transaction list
    """

    def __init__(self, trades: list=None):
        """
        :param trades: list of trades
        """
        self.trades = trades or []

    def add_trade(self, trade: Trade):
        """
        Adds a single trade
        :param trade:
        :return:
        """
        self.trades.append(trade)

    def get_trades_in_interval(self) -> list:
        """
        Returns a list of all trades in the last 15 minutes
        :return:
        """
        interval_start = datetime.now() - timedelta(minutes=15)
        interval_end = datetime.now()
        trades_in_interval = []
        for trade in self.trades:
            if interval_start <= trade.trade_date <= interval_end:
                trades_in_interval.append(trade)

        return trades_in_interval

    @handle_zero_division
    def vol_weighted_stock_price(self) -> float:
        """
        Return the vwsp over a list of trades
        Returns inf if zero division occurs
        :return:
        """
        price_quantity_sum = 0
        quantity_sum = 0

        for trade in self.trades:
            price_quantity_sum += trade.price * trade.volume
            quantity_sum += trade.volume

        return price_quantity_sum / quantity_sum
