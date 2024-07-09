from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np

from Trends.trends import *
from DataFrameSetup.dfsetup import *
from PlotScripts.graphs import *


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return redirect(url_for("stockinfo", ticker = request.form["ticker"]))

@app.route('/<ticker>', methods = ["GET", "POST"])
def stockinfo(ticker):
    
    df = dfgenerator(ticker)

    return render_template('analysis.html', div_html = create_bollinger_graph(df, ticker), bollinger_trend = get_bollinger_trend(df),
                           ticker = ticker, price_rsi = create_RSI_graph(df, ticker), rsi_trend = get_RSI_trend(df.iloc[-1]['RSI']))

@app.route('/about', methods = ["GET", "POST"])
def about():
    return render_template('about.html')
    
@app.route('/contect', methods = ["GET", "POST"])
def contact():

    return render_template('contact.html')
    
                           
