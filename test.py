import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# יצירת נתוני דוגמא
df = pd.DataFrame({
    "קטגוריה": ["A", "B", "C", "D"],
    "ערך": [10, 15, 7, 12]
})

# יצירת אפליקציה
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("דשבורד אינטראקטיבי לדוגמא"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': kat, 'value': kat} for kat in df["קטגוריה"]],
        value='A',
        clearable=False
    ),
    dcc.Graph(id='bar-graph'),
    html.Div(id='value-output', style={'marginTop': 20, 'fontSize': 24})
])


@app.callback(
    [Output('bar-graph', 'figure'),
     Output('value-output', 'children')],
    [Input('category-dropdown', 'value')]
)
def update_dashboard(selected_cat):
    filtered_df = df[df["קטגוריה"] == selected_cat]
    fig = px.bar(filtered_df, x="קטגוריה", y="ערך", title=f"ערך עבור קטגוריה {selected_cat}")
    value_text = f"ערך לקטגוריה {selected_cat}: {filtered_df['ערך'].iloc[0]}"
    return fig, value_text

if __name__ == '__main__':
    app.run_server(debug=True)