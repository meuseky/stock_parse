#!/usr/bin/env python3
import argparse
import sys

from src.analysis import index_analysis, trade_analysis, stock_analysis
from src.lib.file_io import get_csv_data_by_filename
from src.lib.messages import file_not_found_message


def parse_args(input_args):
    """
    Retrieves commandline args
    :param input_args:
    :return:
    """
    parser = argparse.ArgumentParser(
        description="A simple utility to analyse and display "
                    "trade, index, and stock price data from csv files")
    parser.add_argument('--index', '-i',
                        help='Analyses index data from csv file')
    parser.add_argument('--stock', '-s',
                        help='Analyses stock data from csv file')
    parser.add_argument('--trade', '-t',
                        help='Analyses trade data from csv file')
    return parser.parse_args()


def run_analysis(input_args):
    """
    Runs routes selected by args
    :param input_args:
    :return:
    """
    try:
        if input_args.index:
            index_data = get_csv_data_by_filename(input_args.index)
            output_data = index_analysis(index_data)
            for line in output_data:
                print(line)

        if input_args.stock:
            stock_data = get_csv_data_by_filename(input_args.stock)
            output_data = stock_analysis(stock_data)
            for line in output_data:
                print(line)

        if input_args.trade:
            trade_data = get_csv_data_by_filename(input_args.trade)
            output_data = trade_analysis(trade_data)
            for line in output_data:
                print(line)

    except FileNotFoundError as e:
        print(file_not_found_message.format(e.filename))


def main():
    """
    Separate main() function to allow module to be used
    as a console_script
    :return:
    """
    args = parse_args(sys.argv[1:])
    run_analysis(args)

if __name__ == "__main__":
    main()
