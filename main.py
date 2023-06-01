from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the sample CSV file into a DataFrame
df = pd.read_csv('sample.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ips = request.form.getlist('ip_address')
        option = request.form.get('option')

        if option == 'include':
            filtered_df = df[df['IP'].isin(ips)]
        elif option == 'exclude':
            filtered_df = df[~df['IP'].isin(ips)]
        else:
            filtered_df = pd.DataFrame()  # Empty DataFrame if no option is selected

        return render_template('index.html', df=filtered_df)

    return render_template('index.html', df=df)

if __name__ == '__main__':
    app.run(debug=True)
