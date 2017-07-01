#!/usr/bin/env python3
import argparse
import sys

from src.analysis import index_analysis, trade_analysis, stock_analysis
from src.lib.file_io import get_csv_data_by_file
from src.lib.messages import index_string, stock_string, trade_string, \
    csv_error_message


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


def run_analysis(input_args, output=sys.stdout):
    if input_args.index:
        index_data = get_csv_data_by_file(input_args.index)
        output.write("# Index Analysis")
        try:
            index = index_analysis(index_data)
            output.write(index_string.format(index.gbce_all_share_index()))
        except KeyError:
            output.write(csv_error_message)

    if input_args.stock:
        stock_data = get_csv_data_by_file(input_args.stock)
        output.write("# Stock Analysis")
        try:
            stock_list = stock_analysis(stock_data)
            for stock in stock_list:
                output.write(
                    stock_string.format(stock.symbol, stock.dividend_yield(),
                                        stock.pe_ratio()))
        except KeyError:
            output.write(csv_error_message)

    if input_args.trade:
        trade_data = get_csv_data_by_file(input_args.trade)
        output.write("# Trade Analysis")
        try:
            trade_dict = trade_analysis(trade_data)
            for symbol, trades in trade_dict.items():
                output.write(
                    trade_string.format(symbol,
                                        trades.vol_weighted_stock_price()))
        except KeyError:
            output.write(csv_error_message)


def main():
    args = parse_args(sys.argv[1:])
    if args.output:
        run_analysis(args, args.output)
    else:
        run_analysis(args)

if __name__ == "__main__":
    main()
