# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:38:31 2022

@author: Satya
"""

%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
mpl_fig, ax = plt.subplots()
ax.scatter(x=[1, 2, 3], y=[23, 12, 34])
plotly_fig = mpl_to_plotly(mpl_fig)
plotly_fig

pip install dash


import dash
## import dash_html_components as html
from dash import html
app = dash.Dash(__name__)
#Create the app's layout:

    app.layout = html.Div([
                      html.H1('Hello, World!')
                        ])
#4. Run the app:
if __name__ == '__main__':
    app.run_server(debug=True)