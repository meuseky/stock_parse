import argparse
from io import StringIO
from unittest import TestCase

from mock import patch

from src.domain.index import Index
from src.stock_parse import run_analysis


class TestApp(TestCase):

    def setUp(self):
        self.args = argparse.Namespace()
        self.args.index = None
        self.args.stock = None
        self.args.trade = None

    @patch("src.stock_parse.index_analysis")
    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_index(self, get_csv_file, get_index):
        self.args.index = "index_file.csv"
        index_data = [{
            "symbol": "ABC",
            "price": 100
        }]
        get_csv_file.return_value = index_data

        run_analysis(self.args)
        get_index.assert_called_with(index_data)

    @patch("src.stock_parse.stock_analysis")
    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_stock(self, get_csv_file, get_stock):
        self.args.stock = "stock_file.csv"
        stock_data = [{
            "symbol": "ABC",
            "type": "common",
            "last_dividend": 15.0,
            "fixed_dividend": "",
            "par_value": 100,
            "price": 50.0,
        }]
        get_csv_file.return_value = stock_data

        run_analysis(self.args)
        get_stock.assert_called_with(stock_data)

    @patch("src.stock_parse.trade_analysis")
    @patch("src.stock_parse.get_csv_data_by_file")
    def test_run_analysis_trade(self, get_csv_file, get_trade):
        self.args.trade = "trade_file.csv"
        trade_data = [{
            "symbol": "ALE",
            "price": 70.44,
            "volume": 1000.0,
            "trade_type": "sell",
            "trade_date": "29-06-2017 22:34:00"
        }]
        get_csv_file.return_value = trade_data

        run_analysis(self.args)
        get_trade.assert_called_with(trade_data)
