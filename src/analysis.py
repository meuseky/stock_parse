from src.domain.index import Index, IndexStock
from src.domain.stock import Stock
from src.domain.trade import Trade, TradeList


def index_analysis(index_data):
    """
    Returns Index class containing GBCE All Share Index method
    :param index_data:
    :return:
    """
    index = Index()

    for data in index_data:
        index_stock = IndexStock(data["symbol"], data["price"])
        index.add_index_stock(index_stock)

    return index


def stock_analysis(stock_data):
    """
    Returns list of stocks with Div Yiels, and PE Ratio methods
    :param stock_data:
    :return:
    """
    stock_list = []

    for data in stock_data:
        stock = Stock(data["symbol"], data["type"],
                      data["last_dividend"], data["fixed_dividend"],
                      data["par_value"], data["price"])
        stock_list.append(stock)

    return stock_list


def trade_analysis(trade_data):
    """
    Returns dict of Trade Lists with Volume Weighted Prices
    :param trade_data:
    :return:
    """
    trade_dict = {}

    for data in trade_data:
        symbol = data["symbol"]
        trade = Trade(symbol, data["price"], data["volume"],
                      data["trade_type"], data["trade_date"])

        if symbol not in trade_dict:
            trade_dict[symbol] = TradeList()
        trade_dict[symbol].add_trade(trade)

    for symbol in trade_dict.keys():
        trades_in_interval = [t for t in
                              trade_dict[symbol].get_trades_in_interval()]
        trade_dict[symbol] = TradeList(trades_in_interval)

    return trade_dict


