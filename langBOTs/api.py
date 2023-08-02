import nltk
from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok #add token tho or else weird e
from flask_cors import CORS



import locale
locale.getpreferredencoding = lambda: "UTF-8"  #dunno why

nltk.download('punkt')  # Download the Punkt tokenizer if not already downloaded



app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

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

@app.route('/api/second_string', methods=['POST', 'OPTIONS'])
def process_second_string():
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers
    ##
    data = request.get_json()
    print(data)
    second_string = data['second_string']
    result = qury(second_string)
    # Process the second string and generate the result
    result = nltk.sent_tokenize(result)[:1]
    print(result)
    return jsonify({'second_string': result})

def start():
    app.run()
