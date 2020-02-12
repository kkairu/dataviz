# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper, HoverTool, Paragraph,
						  ColumnDataSource, Panel, 
						  FuncTickFormatter, SingleIntervalTicker, LinearAxis)
from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider, 
								  Tabs, CheckboxButtonGroup, 
								  TableColumn, DataTable, Select)
from bokeh.layouts import column, row, WidgetBox
from bokeh.palettes import Category20_16

# Make plot with histogram and return tab
def forecast_tab(data, ticker):

	pg_title = Paragraph()
	pg_title.text = '[ '+ticker+' ] CLOSE PRICE FORECAST'

	# Create a row layout
	layout = row(pg_title)
	
	# Make a tab with the layout 
	tab = Panel(child=layout, title = 'Forecast')

	return tab