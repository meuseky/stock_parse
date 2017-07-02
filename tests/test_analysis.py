from datetime import datetime
from unittest import TestCase

from src.analysis import stock_analysis, trade_analysis, index_analysis
from src.domain.trade import trade_date_format
from src.lib.messages import csv_error_message, data_error_message


class TestAnalysis(TestCase):

    def test_index_analysis(self):
        index_data = [{
            "symbol": "ABC",
            "price": 100
        }]

        expected_result = [
            '# Index Analysis',
            'GBCE All Share Index: 100.000000'
        ]
        actual_result = index_analysis(index_data)
        self.assertEqual(expected_result, actual_result)

    def test_index_analysis_key_error(self):
        expected_result = [
            csv_error_message
        ]

        # Missing key in input data
        actual_result = index_analysis([{
            "symbol": "ABC"
        }])
        self.assertEqual(expected_result, actual_result)

    def test_index_analysis_type_error(self):
        expected_result = [
            data_error_message
        ]

        # Price is input as a string instead of a float
        actual_result = index_analysis([{
            "symbol": "ABC",
            "price": "100"
        }])
        self.assertEqual(expected_result, actual_result)

    def test_stock_analysis(self):
        stock_data = [{
            "symbol": "ABC",
            "type": "common",
            "last_dividend": 15.0,
            "fixed_dividend": "",
            "par_value": 100,
            "price": 50.0,
        }]

        expected_result = [
            '# Stock Analysis',
            'Symbol: ABC | Dividend Yield: 0.300000 | PE Ratio: 3.333333'
        ]
        actual_result = stock_analysis(stock_data)
        self.assertEqual(expected_result, actual_result)
        
    def test_stock_analysis_key_error(self):
        expected_result = [
            csv_error_message
        ]

        # Missing key in input data
        actual_result = stock_analysis([{
            "symbol": "ABC"
        }])
        self.assertEqual(expected_result, actual_result)

    def test_stock_analysis_type_error(self):
        expected_result = [
            data_error_message
        ]

        # Price is input as a string instead of a float
        actual_result = stock_analysis([{
            "symbol": "ABC",
            "type": "common",
            "last_dividend": 15.0,
            "fixed_dividend": "",
            "par_value": 100,
            "price": "50.0",
        }])
        self.assertEqual(expected_result, actual_result)

    def test_trade_analysis(self):
        trade_data = [{
            "symbol": "ALE",
            "price": 70.44,
            "volume": 1000.0,
            "trade_type": "sell",
            "trade_date": "29-06-2017 22:34:00"
        }]

        expected_result = [
            '# Trade Analysis',
            'Symbol: ALE | Volume Weighted Price: inf'
        ]
        actual_result = trade_analysis(trade_data)
        self.assertEqual(expected_result, actual_result)
        
    def test_trade_analysis_key_error(self):
        expected_result = [
            csv_error_message
        ]

        # Missing key in input data
        actual_result = trade_analysis([{
            "symbol": "ALE"
        }])

        self.assertEqual(expected_result, actual_result)

    def test_trade_analysis_type_error(self):
        expected_result = [
            data_error_message
        ]

        # Price is input as a string instead of a float
        actual_result = trade_analysis([{
            "symbol": "ALE",
            "price": "70.44",
            "volume": 1000.0,
            "trade_type": "sell",
            "trade_date": datetime.now().strftime(trade_date_format)
        }])
        self.assertEqual(expected_result, actual_result)