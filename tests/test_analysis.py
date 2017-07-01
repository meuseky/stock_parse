from unittest import TestCase

from src.analysis import stock_analysis, trade_analysis, index_analysis


class TestAnalysis(TestCase):
        
    def test_index_analysis_key_error(self):
        index_data = [{
            "symbol": "ABC"
        }]
        self.assertRaises(KeyError, index_analysis, index_data)
        
    def test_stock_analysis_key_error(self):
        stock_data = [{
            "symbol": "ABC"
        }]
        self.assertRaises(KeyError, stock_analysis, stock_data)
        
    def test_trade_analysis_key_error(self):
        trade_data = [{
            "symbol": "ALE"
        }]
        self.assertRaises(KeyError, trade_analysis, trade_data)
