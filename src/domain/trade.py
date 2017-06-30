from datetime import datetime

from src.lib.decorator import handle_zero_division


class Trade(object):
    """
    Put some details here
    """

    def __init__(self, symbol: str, price: float, volume: int,
                 trade_type: str, trade_date: str,
                 date_format: str="%d-%m-%Y %H:%M:%S"):
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
    Put some details here
    """

    def __init__(self, trades: list=None):
        """
        :param trades: list of trades
        """
        self.trades = trades or []

    def add_trade(self, trade: Trade):
        """

        :param trade:
        :return:
        """
        self.trades.append(trade)

    def get_trades_in_interval(self,
                               interval_start: datetime,
                               interval_end: datetime=datetime.now()) -> list:
        """

        :param interval_start:
        :param interval_end:
        :return:
        """
        valid_trades = []
        for trade in self.trades:

            if interval_start <= trade.trade_date <= interval_end:
                valid_trades.append(trade)

        return TradeList(valid_trades)

    @handle_zero_division
    def vol_weighted_stock_price(self) -> float:
        """

        :return:
        """
        price_quantity_sum = 0
        quantity_sum = 0

        for trade in self.trades:
            price_quantity_sum += trade.price * trade.volume
            quantity_sum += trade.volume

        return price_quantity_sum / quantity_sum
