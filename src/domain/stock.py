from src.domain.trade import TradeList, Trade
from src.lib.decorator import handle_zero_division


class Stock(object):
    """
    Put some details here
    """

    def __init__(self, symbol: str, stock_type: str, last_dividend: float,
                 fixed_dividend: float, par_value: float, price: float):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.price = price
        self.trade_list = TradeList()

    def add_trade(self, trade: Trade):
        self.trade_list.add_trade(trade)

    @handle_zero_division
    def dividend_yield(self) -> float:
        """

        :return:
        """
        if self.stock_type == "common":
            numerator = self.last_dividend
        else:
            numerator = self.fixed_dividend * self.par_value
        return numerator / self.price

    @handle_zero_division
    def pe_ratio(self) -> float:
        """

        :return:
        """
        return self.price / self.last_dividend


