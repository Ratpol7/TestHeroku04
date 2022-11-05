from line_notify import LineNotify
from flask import Flask, jsonify
import pandas as pd
import os
import mplfinance as mpf
import matplotlib.pyplot as plt
import yfinance as yf
df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})

Line_Notify = str(os.getenv('Line_Notify_Token'))
# Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)

app = Flask(__name__)

@app.route('/')
def hello_view():
    notify.send("TestDeploy", sticker_id=17851, package_id=1070)
    return "<h1>Hello World!<h1>"

@app.route('/pandas')
def pandas():
    return df.to_html(header="true", table_id="table")

@app.route('/yfinance')
def yfinance():
    yahoo_financials = yf('BTC-USD')
    data=yahoo_financials.get_historical_price_data("2019-07-10", "2021-05-30", "monthly")
    btc_df = pd.DataFrame(data['BTC-USD']['prices'])
    return btc_df.to_html(header="true", table_id="table")

    
if __name__ == "__main__":
    # app.run(host='0.0.0.0',port=80,debug=True)
    app.run()

