from unittest import TestCase
from mock import patch

from src.domain.index import Index, IndexStock


class TestIndex(TestCase):

    def test_index_stock_sufficient_args(self):
        symbol = "ABC"
        price = 1.23
        IndexStock(symbol, price)

    def test_index_stock_insufficient_args(self):
        symbol = "ABC"
        self.assertRaises(Exception, IndexStock, symbol)

    def test_index_sufficient_args(self):
        index_stocks = []
        Index(index_stocks)

    def test_index_no_args(self):
        # Test that no exception is raised when class without params
        Index()

    def test_add_index_stock(self):
        index = Index()
        self.assertEqual(0, len(index.index_stocks))

        index.add_index_stock(IndexStock("ABC", 1.23))
        self.assertEqual(1, len(index.index_stocks))

    def test_get_price_list(self):
        index = Index()
        self.assertEqual([], index.get_price_list())

        index_stock_data = {
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5
        }
        for symbol, price in index_stock_data.items():
            index.add_index_stock(IndexStock(symbol, price))
        self.assertEqual([1, 2, 3, 4, 5], index.get_price_list())

    @patch("src.domain.index.Index.get_price_list")
    def test_gbce_all_share_index(self, price_list):
        index = Index()

        price_list.return_value = []
        self.assertEqual(0, index.gbce_all_share_index())

        price_list.return_value = [1, 2, 3, 4, 5]
        self.assertEqual(2.605171084697352, index.gbce_all_share_index())
