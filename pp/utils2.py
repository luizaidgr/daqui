import dash
import dash_html_components as html
import dash_core_components as dcc
import pathlib
import pandas as pd


df_fund_facts = pd.read_csv('https://raw.githubusercontent.com/luizaidgr/daqui/master/34691362000198/df_fund_facts.csv',sep=',')
name = df_fund_facts.iloc[0, 1]


df_series = pd.read_csv('https://raw.githubusercontent.com/luizaidgr/daqui/master/34691362000198/Series.csv',sep=',')
df_series['Date'] = pd.to_datetime(df_series.Date, format="%Y%m%d")
data_hje = df_series['Date'].max().strftime('%d/%b/%Y')


def Header(app):
    return html.Div(
        [get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(id="idz"),

            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dash-financial-logo.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("IDGR Web", id="learn-more-button"),
                        href="http://www.idgr.com.br/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        html.H5(html.P(id='nome_fundo_FIDC', children=name)),
                        # html.H6(data_hje)
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            # dcc.Location(id='url', refresh=False),
                            dcc.Link(
                                "Full View",
                                href="/Laminas/FIDC6n",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            # dcc.Location(id='url', refresh=False),
            dcc.Link(

                "Geral",
                href="/Laminas/FIDCn",
                className="tab first",
            ),
            dcc.Link(id="concentracao",

                        children="Concentração",
                     href="/Laminas/FIDC2n",
                     className="tab",
                     ),
            # dcc.Link(
            #    "Caixa e Custos",
            #    href="/Laminas/FIDC1",
            #    className="tab",
            # ),
            dcc.Link(
                "Performance", href="/Laminas/FIDC4n", className="tab"
            ),

            dcc.Link(
                "Atraso e PDD",
                href="/Laminas/FIDC3n",
                className="tab",
            ),
            dcc.Link(
                "Lâmina Comercial",
                href="/Laminas/FIDC7",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
