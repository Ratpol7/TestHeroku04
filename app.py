from line_notify import LineNotify
from flask import Flask, jsonify
import pandas as pd
import os
import time
from datetime import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import numpy
import requests
df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})
data = yf.download("BTC", start="2017-01-01", end="2017-04-30")
Line_Notify = str(os.getenv('Line_Notify_Token'))
# Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)

app = Flask(__name__)

@app.route('/')
def hello_view():
    notify.send("TestDeploy", sticker_id=17851, package_id=1070)
    return "<h1>Hello World!<h1>"

@app.route('/1')
def pandas():
    return  data.head()
    # return df.to_html(header="true", table_id="table")
# st.set_page_config(page_title="US Stock Analysis",)
# st.write("""##### Closing Price""")

# @app.route('/2')
# def yfinance():

#     return btc_df.to_html(header="true", table_id="table")


if __name__ == "__main__":
    # app.run(host='0.0.0.0',port=80,debug=True)
    app.run()

