from functools import reduce
from operator import attrgetter


class IndexStock(object):
    """
    Represents a single stock in an Index
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
    A list of IndexStocks with a method returning the GBCE Index
    """

    def __init__(self, index_stocks: list=None):
        """
        :param index_stocks:
        :return:
        """
        self.index_stocks = index_stocks or []

    def add_index_stock(self, index_stock: IndexStock):
        """
        Adds a single IndexStock to the Index
        :param index_stock:
        :return:
        """
        self.index_stocks.append(index_stock)

    def get_price_list(self) -> list:
        """
        Returns a list of all of the prices of stocks in the Index
        :return:
        """
        return list(map(attrgetter('price'), self.index_stocks))

    def gbce_all_share_index(self) -> float:
        """
        Returns the geometric mean of the Index price list
        :return:
        """
        price_list = self.get_price_list()
        if not price_list:
            return 0

        price_multiplicand = reduce(lambda x, y: x*y, price_list)
        root = 1.0 / len(price_list)
        return price_multiplicand**root
