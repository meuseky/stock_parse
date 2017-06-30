from unittest import TestCase

from src.domain.trade import Trade, TradeList


class TestTrade(TestCase):

    def setUp(self):
        self.symbol = "ABC"
        self.price = 1.23
        self.volume = 1000
        self.trade_type = "buy"
        self.trade_date = "01-01-2000 12:00:00"
    
    def test_trade_sufficient_args(self):
        Trade(self.symbol, self.price, self.volume, self.trade_type, self.trade_date)

    def test_trade_invalid_date_format(self):
        invalid_trade_date = "01/01/2000"
        self.assertRaises(ValueError, Trade, self.symbol, self.price, self.volume, self.trade_type,
                          invalid_trade_date)

    def test_trade_list_insufficient_args(self):
        self.assertRaises(Exception, Trade, self.symbol)

    def test_trade_list_sufficient_args(self):
        trades = []
        TradeList(trades)

    def test_trade_no_args(self):
        # Test that no exception is raised when class initialised without params
        TradeList()
    #
    # def test_add_trade(self):
    #     self.fail()
    #
    # def test_get_trades_in_interval(self):
    #     self.fail()
    #
    # def test_vol_weighted_stock_price(self):
    #     self.fail()
