from os.path import dirname, join

import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

# Default ticker
TICKER = 'SCOM'

@st.cache # Data only downloaded once and cached for future use

def get_ticker_data():
    
    ticker_file = TICKER+'.csv'

    # Read data into dataframes
    data_df = pd.read_csv(join('../', 'data', ticker_file), parse_dates=True).dropna()

    data_df['Date'] = pd.to_datetime(data_df['Date'])

    return data_df


data_df = get_ticker_data()

# Show last 5 transactions in data
st.header('**StockSight** - [ '+TICKER+' ] Share Price Analysis')
st.markdown('The last 5 records of **[ '+TICKER+' ]** data downloaded.')
st.dataframe(data_df.tail(3).sort_values(by=['Date'], ascending=False))


# Show historical data trend
st.header('Historical Close Price Trend')

values = st.sidebar.slider("Data Index Range", int(data_df.index[0]), int(data_df.index[-1]),(int(data_df.index[0]),int(data_df.index[-1])))

fig = px.line(data_df.query(f"index.between{values}"), x='Date', y='Close')

fig.update_xaxes(title="Trading Date")
fig.update_yaxes(title="Stock Close Price (KES)")

st.plotly_chart(fig)