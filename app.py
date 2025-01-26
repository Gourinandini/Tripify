from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
data_path = 'data/kerala_data.csv'
df = pd.read_csv(data_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booknow')
def booknow():
    # Get unique districts from the dataset
    districts = df['District'].unique()

    # Pass the districts list to the booknow template
    return render_template('booknow.html', districts=districts)

@app.route('/get-data')
def get_data():
    # Get the selected district from the query parameters
    district = request.args.get('district')

    # Filter the dataset based on the district
    filtered_data = df
    if district:
        filtered_data = filtered_data[filtered_data['District'] == district]

    # Convert the filtered data into a dictionary
    filtered_data_dict = filtered_data.to_dict(orient='records')

    # If no data is found for the selected district, display a message
    if not filtered_data_dict:
        return render_template('display_data.html', data=None, message="No data found for the selected district.")
    
    # Return the filtered data to display in the new page
    return render_template('display_data.html', data=filtered_data_dict)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
