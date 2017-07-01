import argparse
from io import StringIO
from unittest import TestCase

from mock import patch

from src.stock_parse import run_analysis


class TestApp(TestCase):

    def setUp(self):
        self.args = argparse.Namespace()
        self.args.index = None
        self.args.stock = None
        self.args.trade = None

    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_index(self, get_csv_file):
        self.args.index = "index_file.csv"
        get_csv_file.return_value = [{
            "symbol": "ABC",
            "price": 100
        }]
        out = StringIO()
        run_analysis(self.args, out)
        
        expected_result = "# Index AnalysisGBCE All Share Index: 100.000000"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)

    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_stock(self, get_csv_file):
        self.args.stock = "stock_file.csv"
        get_csv_file.return_value = [{
            "symbol": "ABC",
            "type": "common",
            "last_dividend": 15.0,
            "fixed_dividend": "",
            "par_value": 100,
            "price": 50.0,
        }]
        out = StringIO()
        run_analysis(self.args, out)

        expected_result = "# Stock AnalysisSymbol: ABC | " \
                          "Dividend Yield: 0.300000 | PE Ratio: 3.333333"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)

    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_trade(self, get_csv_file):
        self.args.trade = "trade_file.csv"
        get_csv_file.return_value = [{
            "symbol": "ALE",
            "price": 70.44,
            "volume": 1000.0,
            "trade_type": "sell",
            "trade_date": "29-06-2017 22:34:00"
        }]
        out = StringIO()
        run_analysis(self.args, out)

        expected_result = "# Trade AnalysisSymbol: ALE | " \
                          "Volume Weighted Price: 70.440000"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)

    @patch("src.stock_parse.get_csv_data_by_file")
    @patch("src.stock_parse.index_analysis")
    def test_run_analysis_index_exception(self, get_index, get_csv_file):
        self.args.index = "index_file.csv"
        get_csv_file.return_value = []
        get_index.side_effect = KeyError
        out = StringIO()
        run_analysis(self.args, out)

        expected_result = "# Index AnalysisError - Invalid CSV File"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)

    @patch("src.stock_parse.get_csv_data_by_file")
    @patch("src.stock_parse.stock_analysis")
    def test_run_analysis_stock_exception(self, get_stock, get_csv_file):
        self.args.stock = "stock_file.csv"
        get_csv_file.return_value = []
        get_stock.side_effect = KeyError
        out = StringIO()
        run_analysis(self.args, out)

        expected_result = "# Stock AnalysisError - Invalid CSV File"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)

    @patch("src.stock_parse.get_csv_data_by_file")
    @patch("src.stock_parse.trade_analysis")
    def test_run_analysis_trade_exception(self, get_trade, get_csv_file):
        self.args.trade = "trade_file.csv"
        get_csv_file.return_value = []
        get_trade.side_effect = KeyError
        out = StringIO()
        run_analysis(self.args, out)

        expected_result = "# Trade AnalysisError - Invalid CSV File"
        actual_result = out.getvalue().strip()
        self.assertEqual(expected_result, actual_result)
