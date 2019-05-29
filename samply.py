import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
import plotly.figure_factory as FF


from IPython.display import IFrame
df = pd.read_csv('sample-data.csv')
print(df)

#

sample_data_table = FF.create_table(df.head())
#py.iplot(sample_data_table, filename='sample-data-table')

plotly.offline.plot({"data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
     "layout": go.Layout(title="hello world")})


trace1 = go.Scatter(x=df['x'], y=df['logx'], # Data
                     mode='lines', name='logx')

trace2 = go.Scatter(x=df['x'], y=df['sinx'], mode='lines', name='sinx' )
trace3 = go.Scatter(x=df['x'], y=df['cosx'], mode='lines', name='cosx')

layout = go.Layout(title='Simple Plot from csv data',
                    plot_bgcolor='rgb(230, 230,230)')
fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
plotly.offline.plot(fig, filename='simple-plot-from-csv')

###

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')


df_external_source = FF.create_table(df.head())



plotly.offline.plot(df_external_source, filename='df-external-source-table')
trace = go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                   name='Share Prices (in USD)')

layout = go.Layout(title='Apple Share Prices over time (2014)',
                    plot_bgcolor='rgb(230, 230,230)',
                    showlegend=True)

fig = go.Figure(data=[trace], layout=layout)

plotly.offline.plot(fig, filename='apple-stock-prices.html')
'apple-stock-prices.html'
