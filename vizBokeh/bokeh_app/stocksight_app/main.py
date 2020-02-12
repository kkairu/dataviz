# Pandas for data management
import pandas as pd

# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs


# Each tab is drawn by one script
from scripts.trend import trend_tab
from scripts.forecast import forecast_tab
from scripts.download import download_tab

#Default ticker
ticker = 'SCOM'
ticker_file = ticker+'.csv'

# Read data into dataframes
data_df = pd.read_csv(join(dirname(__file__), 'data', ticker_file), parse_dates=True).dropna()

data_df['Date'] = pd.to_datetime(data_df['Date'])

# Create each of the tabs
tab1 = trend_tab(data_df, ticker)
tab2 = forecast_tab(data_df, ticker)
tab3 = download_tab(data_df, ticker)

# Put all the tabs into one application
tabs = Tabs(tabs = [tab1, tab2, tab3])

# Put the tabs in the current document for display
stocksight = curdoc()
stocksight.add_root(tabs)
stocksight.title = 'StockSight App'