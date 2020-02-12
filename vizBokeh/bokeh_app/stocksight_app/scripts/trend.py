# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from bokeh.layouts import gridplot, column, row, widgetbox
from bokeh.models import Panel, Paragraph
from bokeh.plotting import figure, show, output_file
from bokeh.models.widgets import Dropdown

# Make plot with histogram and return tab
def trend_tab(data, ticker):

	#pg_title = Paragraph()
	#pg_title.text = '[ '+ticker+' ] PRICE TREND'

	def make_plot(data_src):

		p = figure(x_axis_type="datetime", title=ticker+' Closing Price Trend', plot_width=800, plot_height=400)
		p.grid.grid_line_alpha=0.3
		p.xaxis.axis_label = 'Trading Date'
		p.yaxis.axis_label = '[ '+ticker+' ] Close Price'

		p.line(data_src['Date'], data_src['Close'], line_width=2, legend_label=ticker)

		p.legend.location = "top_left"

		return p
	
	
	
	def update(attr, old, new):
		# ticker
		ticker = dropdown.value #'SCOM'
		ticker_file = ticker+'.csv'

		# Read data into dataframes
		data_df = pd.read_csv(join(dirname(__file__), 'data', ticker_file), parse_dates=True).dropna()

		data_df['Date'] = pd.to_datetime(data_df['Date'])	

		src.data.update(data_df.data)


	# Set dropdown
	stocks_list = [("Safaricom Plc", "SCOM"), ("Nation Media Group Plc", "NMG"), None, ("Kenya Power & Lighting Company", "KPLC")]
	dropdown = Dropdown(label="NSE Stocks List", menu=stocks_list)
	
	dropdown.on_change('value', update)
	dropdown.on_click(update)


	p = make_plot(data)
	
	# Create a row layout
	layout = row(widgetbox(dropdown, align='center'), p)
	
	# Make a tab with the layout 
	tab = Panel(child=layout, title = 'Stock Price Trend')

	return tab