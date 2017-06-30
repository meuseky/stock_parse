from math import inf
from unittest import TestCase

from src.domain.stock import Stock
from src.domain.trade import Trade


class TestStock(TestCase):

    def setUp(self):
        self.symbol = "ABC"
        self.stock_type = "common"
        self.last_dividend = 10
        self.fixed_dividend = 0.01
        self.par_value = 100
        self.price = 50
        self.stock = Stock(self.symbol, self.stock_type, self.last_dividend,
                           self.fixed_dividend, self.par_value, self.price)

    def test_stock_insufficient_args(self):
        self.assertRaises(Exception, Stock, self.symbol)

    def test_add_trade(self):
        self.assertEqual(0, len(self.stock.trade_list.trades))

        self.stock.add_trade(Trade("ABC", 1.23, 1000, "buy", "01-01-2000 12:00:00"))
        self.assertEqual(1, len(self.stock.trade_list.trades))

    def test_dividend_yield(self):
        # "common" stock
        self.assertEqual(0.2, self.stock.dividend_yield())

        # "preferred" stock
        self.stock.stock_type = "preferred"
        self.assertEqual(0.02, self.stock.dividend_yield())

    def test_dividend_yield_zero_division(self):
        self.stock.price = 0
        self.assertEqual(inf, self.stock.dividend_yield())

    def test_pe_ratio(self):
        self.assertEqual(5, self.stock.pe_ratio())

    def test_pe_ratio_zero_division(self):
        self.stock.last_dividend = 0
        self.assertEqual(inf, self.stock.pe_ratio())
