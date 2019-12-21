import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_excel("Dashboard - Project Tracking.xlsx", nrows=14,
                   skiprows=1, index_col=0)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='RESCO I', value='tab-1'),
        dcc.Tab(label='RESCO II', value='tab-2'),
        dcc.Tab(label='RESCO III', value='tab-3'),
        dcc.Tab(label='EPC', value='tab-4'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('RESCO I content')
        ])
        return dash_table.DataTable(id='table',
                                    columns=[{"name": i, "id": i}
                                             for i in df.columns],
                                    data=df.to_dict('records'))
    elif tab == 'tab-2':
        return html.Div([
            html.H3('RESCO II content')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('RESCO III content')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('EPC content')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
