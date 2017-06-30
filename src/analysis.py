from src.domain.index import Index, IndexStock
from src.domain.stock import Stock
from src.domain.trade import Trade, TradeList

index_string = "GBCE All Share Index: {:f}"
stock_string = "Symbol: {} | Dividend Yield: {:f} | PE Ratio: {:f}"
trade_string = "Symbol: {} | Volume Weighted Price: {:f}"


def index_analysis(index_data):
    index = Index()
    for data in index_data:
        index_stock = IndexStock(data["symbol"], data["price"])
        index.add_index_stock(index_stock)

    print(index_string.format(index.gbce_all_share_index()))


def stock_analysis(stock_data):
    stock_list = []
    for data in stock_data:
        stock = Stock(data["symbol"], data["type"], data["last_dividend"],
                      data["fixed_dividend"], data["par_value"], data["price"])
        stock_list.append(stock)

    for stock in stock_list:
        print(stock_string.format(stock.symbol, stock.dividend_yield(), stock.pe_ratio()))


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
    for symbol, trades in trade_dict.items():
        print(trade_string.format(symbol, trades.vol_weighted_stock_price()))
