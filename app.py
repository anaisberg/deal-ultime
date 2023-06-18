from flask_cors import CORS
from getData import get_data
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000', 'localhost:5000'])

# In this case, the URL route is 'getlocations'.
@app.route('/getlocations', methods=['GET'])
def displaylocations():
     # get the deals data.
    deals = get_data()
    print(deals)
    # Forward the data to the source that called this API.
    response = jsonify(deals)
    return response

if __name__ == '__main__':
    app.run(host='localhost', debug = True, port=5000)