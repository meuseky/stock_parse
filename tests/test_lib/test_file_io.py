from unittest import TestCase

from mock import patch, mock_open
from src.lib.file_io import get_csv_data_by_filename


class TestFile(TestCase):
    csv_file_data = '"one"\n"two"'

    @patch("builtins.open", new_callable=mock_open, read_data=csv_file_data)
    def test_get_csv_data_by_filename(self, mock_open_method):
        get_csv_data_by_filename("ewrr")
