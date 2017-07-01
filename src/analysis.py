from src.domain.index import Index, IndexStock
from src.domain.stock import Stock
from src.domain.trade import Trade, TradeList


def index_analysis(index_data):
    index = Index()

    for data in index_data:
        index_stock = IndexStock(data["symbol"], data["price"])
        index.add_index_stock(index_stock)

    return index


def stock_analysis(stock_data):
    stock_list = []

    for data in stock_data:
        stock = Stock(data["symbol"], data["type"],
                      data["last_dividend"], data["fixed_dividend"],
                      data["par_value"], data["price"])
        stock_list.append(stock)

    return stock_list


def trade_analysis(trade_data):
    trade_dict = {}

    for data in trade_data:
        symbol = data["symbol"]
        trade = Trade(symbol, data["price"], data["volume"],
                      data["trade_type"], data["trade_date"])

        if symbol not in trade_dict:
            trade_dict[symbol] = TradeList()
        trade_dict[symbol].add_trade(trade)
    # Later get only trades in interval

    return trade_dict


