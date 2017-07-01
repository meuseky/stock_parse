from datetime import datetime, timedelta
from math import inf
from unittest import TestCase

from src.domain.trade import Trade, TradeList, trade_date_format


class TestTrade(TestCase):

    def setUp(self):
        self.symbol = "ABC"
        self.price = 1.23
        self.volume = 1000
        self.trade_type = "buy"
        self.trade_date = "01-01-2000 12:00:00"
        self.trade = Trade(self.symbol, self.price, self.volume,
                           self.trade_type, self.trade_date)

    def test_trade_sufficient_args(self):
        Trade(self.symbol, self.price, self.volume,
              self.trade_type, self.trade_date)

    def test_trade_insufficient_args(self):
        self.assertRaises(Exception, Trade, self.symbol)

    def test_trade_invalid_date_format(self):
        invalid_trade_date = "01/01/2000"
        self.assertRaises(ValueError, Trade, self.symbol, self.price,
                          self.volume, self.trade_type, invalid_trade_date)

    def test_trade_list_sufficient_args(self):
        trades = []
        TradeList(trades)

    def test_get_trades_in_interval(self):
        date_now = datetime.now().strftime(trade_date_format)
        in_interval = (datetime.now() - timedelta(minutes=10))\
            .strftime(trade_date_format)
        out_of_interval = (datetime.now() - timedelta(minutes=20))\
            .strftime(trade_date_format)

        trade_list = TradeList()
        trade_list.add_trade(Trade(self.symbol, self.price, self.volume,
                                   self.trade_type, date_now))
        trade_list.add_trade(Trade(self.symbol, self.price, self.volume,
                                   self.trade_type, in_interval))
        trade_list.add_trade(Trade(self.symbol, self.price, self.volume,
                                   self.trade_type, out_of_interval))

        trades_in_interval = tuple(trade_list.get_trades_in_interval())
        self.assertEqual(2, len(trades_in_interval))

    def test_vol_weighted_stock_price(self):
        trade_list = TradeList()
        trade_list.add_trade(Trade(self.symbol, 10, 2,
                                   self.trade_type, self.trade_date))
        trade_list.add_trade(Trade(self.symbol, 50, 1,
                                   self.trade_type, self.trade_date))
        trade_list.add_trade(Trade(self.symbol, 5, 10,
                                   self.trade_type, self.trade_date))

        self.assertEqual(9.23076923076923,
                         trade_list.vol_weighted_stock_price())

    def test_vol_weighted_stock_price_zero_division(self):
        trade_list = TradeList()
        trade_list.add_trade(Trade(self.symbol, 10, 0,
                                   self.trade_type, self.trade_date))

        self.assertEqual(inf, trade_list.vol_weighted_stock_price())
