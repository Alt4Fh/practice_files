from dash import Dash, html, dash_table, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_mantine_components as dmc


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = dmc.Container([
    dmc.Title('My First App with Data, Graph, and Controls', size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
    dmc.Grid([
        dmc.GridCol([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.GridCol([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)


# Add controls to build the interaction 
@callback( Output(component_id='graph-placeholder', component_property='figure'),
          Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig
    

if __name__ == '__main__':
    app.run(debug=True)