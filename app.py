import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'laughterRx'
myheading1 = 'Laughter is the BEST Medicine'
myheading2 = 'A Brief Guide on Not Taking Yourself Seriously'
image1 = 'body.jpg'
image2 = 'shower.jpg'
textbody = "Please Don't Touch My Arm with Your Arm: How I Died on Public Transportation"
sourceurl = 'https://www.google.com/search?q=humor+images&oq=humor+images&aqs=chrome..69i57j0l5.2303j1j8&sourceid=chrome&ie=UTF-8'
githublink = 'https://github.com/calijason76/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '12px',
                'font-size': '22px',
                'height': '120px',
                'border': 'thin red solid',
                'color': 'rgb(255, 255, 255)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'right',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
