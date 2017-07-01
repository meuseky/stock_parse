#!/usr/bin/env python3
import argparse
import sys

from src.analysis import index_analysis, trade_analysis, stock_analysis
from src.lib.file_io import get_csv_data_by_file


def parse_args(input_args):
    parser = argparse.ArgumentParser(
        description="A simple utility to analyse and display "
                    "trade, index, and stock price data from csv files")
    parser.add_argument('--index', '-i', type=argparse.FileType('r'),
                        help='Analyses index data from csv file')
    parser.add_argument('--stock', '-s', type=argparse.FileType('r'),
                        help='Analyses stock data from csv file')
    parser.add_argument('--trade', '-t', type=argparse.FileType('r'),
                        help='Analyses trade data from csv file')
    return parser.parse_args()


def run_analysis(input_args):
    if input_args.index:
        index_data = get_csv_data_by_file(input_args.index)
        print("# Index Analysis")
        index_analysis(index_data)

    if input_args.stock:
        stock_data = get_csv_data_by_file(input_args.stock)
        print("# Stock Analysis")
        stock_analysis(stock_data)

    if input_args.trade:
        trade_data = get_csv_data_by_file(input_args.trade)
        print("# Trade Analysis")
        trade_analysis(trade_data)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    run_analysis(args)
