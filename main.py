from flask import Flask, jsonify, request
# I import CORS to solve the CORS problems
from flask_cors import CORS

# i import the function to search
from functions import search
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({'message': 'API is working'})


@app.route('/processing', methods=['POST'])
def processing():
    print('working now')
    print(request.form)
    print(request.form.get('question1'))
    message = request.form.get('question1')
    wikisearch = search.searchword(message)
    return jsonify(wikisearch)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    #app.run()
