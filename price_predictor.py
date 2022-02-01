import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st 
import datetime


st.title("Simple stock predictor")
st.sidebar.header("User inputs")


try:
    def user_input():
        ticker = st.sidebar.text_input(label="Enter the indicator for company: ",
                               value='')
        period_options = ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]
        period = st.sidebar.select_slider(label="Enter the period",options=period_options)
        data = {
            "Stock":ticker,
            "Period":period
        }
        features = pd.DataFrame(data, index=[0])
        return features
    df = user_input()
    st.write("Selected indicators")
    st.write(df)
    
    st.write("Download the data")
    
    for i in df["Stock"]:
        stock = i
    for i in df["Period"]:
        period = i
 
    
    ticker = yf.download(stock, period=period)
    stock = pd.DataFrame(ticker)
    stock.reset_index(inplace = True)
    
    st.write(stock)
    
    st.write("The chart for close")
    st.line_chart(stock.Close)
    
    
    st.write("The predictor based on the data")
    reg = LinearRegression()
    reg.fit(stock["Date"], stock.Close)
    st.write(LinearRegression())
    st.write(reg.coef_)
    
except ValueError:
    print("The indicator is the 4 letter code of company")


