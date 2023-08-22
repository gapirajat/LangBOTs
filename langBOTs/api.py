"""runs flask and executes Query.qury() on /api/second_string route"""
import nltk #to filter output text limiting it to 3 lines
from flask import Flask, jsonify, request #standard flask
from flask_ngrok import run_with_ngrok #add token tho or else weird e
from flask_cors import CORS #had cors error fixed with this

from flask import Flask

import locale
locale.getpreferredencoding = lambda: "UTF-8"  #dunno why but flask wont install without this

nltk.download('punkt')  # Download the Punkt tokenizer for post processing(is it a thing?)

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

#Working on changing urls through api(pretty simple tho)

  
# @app.route('/api/first_string', methods=['POST', 'OPTIONS'])
# def process_first_string():
#     if request.method == 'OPTIONS':
#         # Handle the OPTIONS request
#         response_headers = {
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Methods': 'POST',
#             'Access-Control-Allow-Headers': 'Content-Type'
#         }
#         return '', 200, response_headers
#     ##
#     data = request.get_json()
#     first_string = data['first_string']
#     print(first_string)
#     process_data(first_string)

#     # Process the first string and generate the result
#     result = "sites are loaded !" + urls

#     return jsonify({'first_string': result})

@app.route('/api/query', methods=['POST', 'OPTIONS'])
def process_second_string():
    """Querying and Running  through API.qury()"""
    #CORS
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers


    data = request.get_json()
    print(data)
    second_string = data['query']
    result = Q.qury(second_string)
    # Process the second string and generate the result
    result = nltk.sent_tokenize(result)[:1]
    print(result)
    return jsonify({'second_string': result})

def start(obj):
  global Q
  Q = obj
  app.run() 