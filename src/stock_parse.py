#!/usr/bin/env python3
import argparse

from src.analysis import index_analysis, trade_analysis, stock_analysis
from src.lib.file_io import get_csv_data_by_file

# ---- #---------------------------------------------------------------------#
# Args
# ---- #
parser = argparse.ArgumentParser(
    description="A simple utility to analyse and display "
                "trade, index, and stock price data from csv files")

parser.add_argument('--index', '-i', type=argparse.FileType('r'),
                    help='Analyses index data from csv file')

parser.add_argument('--stock', '-s', type=argparse.FileType('r'),
                    help='Analyses stock data from csv file')

parser.add_argument('--trade', '-t', type=argparse.FileType('r'),
                    help='Analyses trade data from csv file')

args = parser.parse_args()


# ----------- #--------------------------------------------------------------#
# Main script #
# ----------- #
if args.index:
    index_data = get_csv_data_by_file(args.index)
    print("# Index Analysis")
    index_analysis(index_data)

if args.stock:
    stock_data = get_csv_data_by_file(args.stock)
    print("# Stock Analysis")
    stock_analysis(stock_data)

if args.trade:
    trade_data = get_csv_data_by_file(args.trade)
    print("# Trade Analysis")
    trade_analysis(trade_data)

parser.print_help()
