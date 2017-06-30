from functools import reduce
from operator import attrgetter


class IndexStock(object):
    """
    Put some details here
    """

    def __init__(self, symbol: str, price: float):
        """

        :param symbol:
        :param price:
        :return:
        """
        self.symbol = symbol
        self.price = price


class Index(object):
    """
    Put some details here
    """

    def __init__(self, index_stocks: list=None):
        """

        :param index_stocks:
        :return:
        """
        self.index_stocks = index_stocks or []

    def add_index_stock(self, index_stock: IndexStock):
        # TODO type check indexstock? Yes because other methods depend on it being that type
        self.index_stocks.append(index_stock)

    def get_price_list(self) -> list:
        return list(map(attrgetter('price'), self.index_stocks))

    def gbce_all_share_index(self) -> float:
        """

        :return:
        """
        price_list = self.get_price_list()
        if not price_list:
            return 0

        price_multiplicand = reduce(lambda x, y: x*y, price_list)
        root = 1.0 / len(price_list)
        return price_multiplicand**root
