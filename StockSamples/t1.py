import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np

start = datetime.datetime(2016, 1, 6)
end = datetime.datetime.today()

apple = web.DataReader('AAPL', 'yahoo', start, end)
# print(apple.head())

#
import matplotlib.pyplot as plt
#
# #%matplotlib inline
# #pylab inline
# apple['Adj Close'].plot(grid = True)
# plt.show()
microsoft = web.DataReader('MSFT', 'yahoo', start, end)
google = web.DataReader('GOOG', 'yahoo', start, end)

stocks = pd.DataFrame(
    {'AAPL': apple['Adj Close'],
     'MSFT': microsoft['Adj Close'],
     'GOOG': google['Adj Close']
     }
)

#stocks = stocks.apply(lambda x: x / x[0])
# stocks = stocks.apply(lambda  x: np.log(x) - np.log(x.shift(1)))
#
# stocks.plot(grid = True)
# plt.show()

apple['20d'] = apple['Close'].rolling(window=20, center= False).mean()
apple['50d'] = apple['Close'].rolling(window=50, center= False).mean()
apple['20d-50d'] = apple['20d'] - apple['50d']
apple['Regime'] = np.where(apple['20d-50d'] > 0, 1, 0)
apple['Regime'] = np.where(apple['20d-50d'] < 0, -1, apple['Regime'])
# apple.loc['2016-01-01':'2016-08-07',"Regime"].plot(ylim = (-2, 2)).axhline(y=0, color='black', lw=2)
# plt.show()

to_right = True

if to_right:
    regime_orig = apple.ix[-1, "Regime"]
    apple.ix[-1, "Regime"] = 0

apple["Signal"] = np.sign(apple["Regime"] - apple["Regime"].shift(1))

if to_right:
    apple[-1, "Regime"] = regime_orig


# from StockSamples.ohlc_candle import *
# pandas_candlestick_ohlc(apple, otherseries=["20d", "50d", "Signal"])


# apple_adj = apple
# apple_adj_signals = pd.concat([
#             pd.DataFrame({"Price": apple_adj.loc[apple_adj["Signal"] == 1, "Close"],
#                 "Regime": apple_adj.loc[apple_adj["Signal"] == 1, "Regime"],
#                 "Signal": "Buy"}),
#             pd.DataFrame({"Price": apple_adj.loc[apple_adj["Signal"] == -1, "Close"],
#                 "Regime": apple_adj.loc[apple_adj["Signal"] == -1, "Regime"],
#                 "Signal": "Sell"}),
#                 ])
#
# apple_adj_signals.sort_index(inplace = True)
# apple_adj_long_profits = pd.DataFrame({
#             "Price": apple_adj_signals.loc[(apple_adj_signals["Signal"] == "Buy") & apple_adj_signals["Regime"] == 1, "Price"],
#             "Profit": pd.Series(apple_adj_signals["Price"] - apple_adj_signals["Price"].shift(1)).loc[
#                 apple_adj_signals.loc[(apple_adj_signals["Signal"].shift(1) == "Buy") & (apple_adj_signals["Regime"].shift(1) == 1)].index].tolist(),
#             "End Date": apple_adj_signals["Price"].loc[
#                 apple_adj_signals.loc[(apple_adj_signals["Signal"].shift(1) == "Buy") & (apple_adj_signals["Regime"].shift(1) == 1)].index].index
#         })


# to calulate each trade point
apple_tradesignal = pd.concat([
    pd.DataFrame({
        "Price": apple.loc[apple['Signal'] == 1, "Close"],
        "Regime": apple.loc[apple['Signal'] == 1, "Regime"],
        "Signal": "Buy"
    }),
    pd.DataFrame({
        "Price": apple.loc[apple['Signal'] == -1, "Close"],
        "Regime": apple.loc[apple['Signal'] == -1, "Regime"],
        "Signal": "Sell"
    })
    ]
)

apple_tradesignal.sort_index(inplace = True)

# apple_tradesignal["Signal"].shift(1)
#
# apple_profits = pd.DataFrame(
#     {
#         "Price" : apple_tradesignal.loc[
#             apple_tradesignal.loc[apple_tradesignal["Signal"] == "Buy"].index.shift(1)
#                         ]
#         ,
#         "Profit": (apple_tradesignal["Price"] - apple_tradesignal["Price"].shift(1)).loc[
#                     apple_tradesignal["Signal"].shift(1) =="Buy"
#                     ]
#         ,
#         "End Date": 1
#     }, index=[apple_tradesignal.index]
# )

apple_long_profits = pd.DataFrame({
"Price": apple_tradesignal.loc[(apple_tradesignal["Signal"] == "Buy") & (apple_tradesignal["Regime"] == 1), "Price"],

"Profit": pd.Series(apple_tradesignal["Price"] - apple_tradesignal["Price"].shift(1)).loc[
    apple_tradesignal.loc[(apple_tradesignal["Signal"].shift(1) == "Buy") & (apple_tradesignal["Regime"].shift(1) == 1)].index
    ].tolist()
})


#
# m = pd.Series(apple_tradesignal["Price"] - apple_tradesignal["Price"].shift(1)).loc[
#     apple_tradesignal.loc[(apple_tradesignal["Signal"].shift(1) == "Buy") & (apple_tradesignal["Regime"].shift(1) == 1)].index
#     ].tolist()

cash = 10000000
apple_backtest = pd.DataFrame({
    "Start Port. Value" : [],
    "End Port. Value " : [],
    "End Date" : [],
    "Shares" : [],
    "Share Price" : [],
    "Trade Value" : [],
    "Profit per Share" : [],
    "Total Profit" : [],
    "Stop-Loss Triggered" : []
})
#
# port_value = .1
# batch = 100
# stoploss =.2
#
# for index, row in apple_profits.iterrows():
#     batches = np.floor(cash * port_value) // np.ceil(batch * row["Price"])
#     trade_val = batches * batch * row["Price"]
#     if row["Low"] < (1 - stoploss) * row["Price"]:
#         share_profit = np.round((1 - stoploss) * row["Price"], 2)
#         stop_trig = True
#     else:
#         share_profit = row["Profit"]
#         stop_trig = False
#
#     profit = share_profit * batch * batches
#     apple_backtest = apple_backtest.append(
#     pd.DataFrame({
#         "Start Port. Value" : [cash],
#         "End Port. Value " : [cash + profit],
#         "End Date" : row["End Date"],
#         "Shares" : batch * batches,
#         "Share Price" : row["Price"],
#         "Trade Value" : trade_val,
#         "Profit per Share" : share_profit,
#         "Total Profit" : profit,
#         "Stop-Loss Triggered" : stop_trig
#     }, index= [index])
#     )