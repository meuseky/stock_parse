import argparse
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

        run_analysis(self.args)

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

        run_analysis(self.args)

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

        run_analysis(self.args)
