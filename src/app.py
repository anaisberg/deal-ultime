from flask_cors import CORS
from src.getData import get_data
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

# In this case, the URL route is 'getlocations'.
@app.route('/getlocations')
def displaylocations():
     # get the deals data.
    deals = get_data()
    print('deals', deals)
    # Forward the data to the source that called this API.
    return jsonify(deals)

if __name__ == '__main__':
    app.run(debug = True)