import dash_core_components as dcc
import dash_html_components as html
from datetime import date
import dash
import datetime as dt
import pandas as pd
#df_series_pl['Date'] = pd.to_datetime(df_series_pl.Date, format = "%Y%m%d")
#reto_mes['Month'] = reto_mes.index.month
day=date.today().strftime("%Y-%m-%d")
colors = {
    'text': '#7FDBFF'}
def create_layout(app):
    return html.Div([ html.Div(id="ff"),
# represents the URL bar, doesn't render anything

    html.H1(children='Gerar Laminas',
            style={
                    'textAlign': 'center',

                   }
                   ),


    html.Div(id='dlinl1'),





        html.Div(id='dlinl1link'),
                      html.Div([
        dcc.Link('SUBMIT FIDC FENIX', href='/gerarlamina1',className="full-view-linkk",id="submit"),
                      html.Div(id='lala'),
                      html.Div(id='dlinl2link'),
                          ]),
                      html.Div([

                      dcc.Link('SUBMIT FIDC ZEUS', href='/gerarlamina2',className="full-view-linkk"),

                      html.Div(id='lalu')
                          ]),






])

