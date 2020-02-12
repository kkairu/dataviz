# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from bokeh.io import show
from bokeh.models import ColumnDataSource, Panel, Div, Paragraph, DateFormatter, NumberFormatter
from bokeh.models.widgets import TableColumn, DataTable
from bokeh.layouts import column, row


# Show data table
def download_tab(data, ticker):
	
	data_df = ColumnDataSource(data)

	datefmt = DateFormatter(format="dd-M-yyyy")
	pfmt = NumberFormatter(format="0.00")

	# Columns of table
	table_columns = [TableColumn(field='Date', title='Trade Date', formatter=datefmt),
					TableColumn(field='Open', title='Open', formatter=pfmt),
					TableColumn(field='High', title='High', formatter=pfmt),
					TableColumn(field='Low', title='Low', formatter=pfmt),
					TableColumn(field='Close', title='Close', formatter=pfmt),
					TableColumn(field='Change %', title='Change (%)')]

	stocks_data = DataTable(source=data_df, columns=table_columns, width=1000)

	pg_title = Paragraph(text = '[ '+ticker+' ] HISTORICAL DATA')

	about_ticker = Paragraph(text="""Safaricom Plc, formerly Safaricom Limited, is a telecommunications company. 
									The Company provides integrated telecommunication services, including mobile and fixed voice, short messaging service (SMS), data, Internet and M-PESA, 
									a service to send and receive money or pay for goods and services through a mobile phone. 
									
									It also provides financial services and enterprise solutions to businesses and the public sector. 
									The Company's voice services include national and international roaming services. It offers mobile handsets, mobile broadband modems, routers, tablets and notebooks. 
									Its converged business solutions include fixed voice service for corporate and Small and Medium-sized Enterprises (SMEs), mobile solutions and fixed data for homes and businesses using fixed lease lines, 
									and Internet solutions for enterprises and hosted services, such as cloud hosting, domains and security services. 
									The Company offers bill payment, bulk payments and dividend payments..""",
							width=200, height=100)

	disclaimer = Paragraph(text="""Disclaimer:  All investments and trading in the stock market involve risk. 
									Any decisions to place trades in the financial markets, including trading in stock or options or other financial instruments is a personal decision that should only be made after thorough research, 
									including a personal risk and financial assessment and the engagement of professional assistance to the extent you believe necessary. 
									The trading strategies or related information mentioned in this article is for informational purposes only.""")

	layout = column(pg_title, stocks_data, about_ticker, disclaimer)

	tab = Panel(child = layout, title = 'Historical Data')

	return tab