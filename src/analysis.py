from src.domain.index import Index, IndexStock
from src.domain.stock import Stock
from src.domain.trade import Trade, TradeList
from src.lib.messages import index_string, csv_error_message, \
    data_error_message, stock_string, trade_string


def index_analysis(index_data):
    """
    Returns Index class containing GBCE All Share Index method
    :param index_data:
    :return:
    """
    try:
        output_list = ["# Index Analysis"]
        index = Index()
        for data in index_data:
            index_stock = IndexStock(data["symbol"], data["price"])
            index.add_index_stock(index_stock)

        output_list.append(index_string.format(index.gbce_all_share_index()))
        return output_list

    except (KeyError, ValueError):
        return [csv_error_message]

    except TypeError:
        return [data_error_message]


def stock_analysis(stock_data):
    """
    Returns list of stocks with Div Yiels, and PE Ratio methods
    :param stock_data:
    :return:
    """
    try:
        output_list = ["# Stock Analysis"]
        stock_list = []

        for data in stock_data:
            stock = Stock(data["symbol"], data["type"],
                          data["last_dividend"], data["fixed_dividend"],
                          data["par_value"], data["price"])
            stock_list.append(stock)

        for stock in stock_list:
            output_list.append(stock_string.format(stock.symbol,
                                                   stock.dividend_yield(),
                                                   stock.pe_ratio()))
        return output_list

    except (KeyError, ValueError):
        return [csv_error_message]

    except TypeError:
        return [data_error_message]


def trade_analysis(trade_data):
    """
    Returns dict of Trade Lists with Volume Weighted Prices
    :param trade_data:
    :return:
    """
    try:
        output_list = ["# Trade Analysis"]
        trade_dict = {}

        for data in trade_data:
            symbol = data["symbol"]
            trade = Trade(symbol, data["price"], data["volume"],
                          data["trade_type"], data["trade_date"])

            if symbol not in trade_dict:
                trade_dict[symbol] = TradeList()
            trade_dict[symbol].add_trade(trade)

        # Filter trades in interval
        for symbol in trade_dict.keys():
            trades_in_interval = [t for t in
                                  trade_dict[symbol].get_trades_in_interval()]
            trade_dict[symbol] = TradeList(trades_in_interval)

        for symbol, trades in trade_dict.items():
            output_list.append(trade_string.format(symbol,
                               trades.vol_weighted_stock_price()))
        return output_list

    except (KeyError, ValueError):
        return [csv_error_message]

    except TypeError:
        return [data_error_message]
