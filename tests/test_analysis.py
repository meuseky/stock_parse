from unittest import TestCase

from src.analysis import stock_analysis, trade_analysis, index_analysis
from src.domain.index import Index
from src.domain.stock import Stock
from src.domain.trade import TradeList


class TestAnalysis(TestCase):

    def test_index_analysis(self):
        index_data = [{
            "symbol": "ABC",
            "price": 100
        }]
        index_result = index_analysis(index_data)
        self.assertTrue(isinstance(index_result, Index))

    def test_index_analysis_key_error(self):
        index_data = [{
            "symbol": "ABC"
        }]
        self.assertRaises(KeyError, index_analysis, index_data)

    def test_stock_analysis(self):
        stock_data = [{
            "symbol": "ABC",
            "type": "common",
            "last_dividend": 15.0,
            "fixed_dividend": "",
            "par_value": 100,
            "price": 50.0,
        }]
        stock_result = stock_analysis(stock_data)
        self.assertEqual(1, len(stock_result))
        self.assertTrue(isinstance(stock_result[0], Stock))
        
    def test_stock_analysis_key_error(self):
        stock_data = [{
            "symbol": "ABC"
        }]
        self.assertRaises(KeyError, stock_analysis, stock_data)

    def test_trade_analysis(self):
        symbol = "ALE"
        trade_data = [{
            "symbol": symbol,
            "price": 70.44,
            "volume": 1000.0,
            "trade_type": "sell",
            "trade_date": "29-06-2017 22:34:00"
        }]
        trade_result = trade_analysis(trade_data)
        self.assertTrue(isinstance(trade_result[symbol], TradeList))
        
    def test_trade_analysis_key_error(self):
        trade_data = [{
            "symbol": "ALE"
        }]
        self.assertRaises(KeyError, trade_analysis, trade_data)
