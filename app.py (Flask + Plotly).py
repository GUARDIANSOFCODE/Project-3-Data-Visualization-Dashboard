from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Load and process data
    df = pd.read_csv('data/sample_data.csv')
    fig = px.line(df, x='Date', y='Value', title='Sample Data Visualization')
    graph = fig.to_html(full_html=False)

    return render_template('index.html', graph=graph)

if __name__ == "__main__":
    app.run(debug=True)
