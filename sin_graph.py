from flask import Flask
from dash import html, dcc, Dash
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import os

# Initialize the Dash app
app = Dash(__name__)

# Constants
A = 5 # Amplitude
w = 2 * np.pi  # Frequency (angular velocity)

# Time values (from 0 to 1 with 0.01 intervals)
t = np.arange(0, 1.01, 0.01)

# Function values A * sin(wt)
func_values = A * np.cos(w * t)

# Create a DataFrame
df = pd.DataFrame({
    'time': t,
    'Asin(wt)': func_values
})

# Define file path for CSV (use relative paths to avoid issues on different environments)
csv_file_path = os.path.join(os.getcwd(), 'data21.csv')

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

# Load the generated CSV file
df = pd.read_csv(csv_file_path)

# Create the graph layout
app.layout = html.Div([
    html.H1("Graph of A*sin(wt)", style={'textAlign': 'center'}),
    html.H2("made by Aryan Rai", style={'textAlign': 'center'}),
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": df['time'],  # Time values
                    "y": df['Asin(wt)'],  # A*sin(wt) values
                    "type": "line",
                }
            ],
            "layout": {"title": "A*sin(wt) vs Time"},
        },
    )
])

# Flask route to serve the Dash app
@application.route('/')
def render_dashboard():
    return app.index()

# Run Flask server (no need for app.run_server)
if __name__ == '__main__':
    application.run(debug=True)
