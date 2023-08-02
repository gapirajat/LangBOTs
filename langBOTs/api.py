# !pip install flask-ngrok flask-cors

# from flask import Flask, jsonify, request
# from flask_ngrok import run_with_ngrok
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# run_with_ngrok(app)

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
#     process_data(first_string)

#     # Process the first string and generate the result
#     result = first_string.upper()  # Example: Convert the string to uppercase

#     return jsonify({'first_string': result})

# @app.route('/api/second_string', methods=['POST', 'OPTIONS'])
# def process_second_string():
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
#     print(data)
#     second_string = data['second_string']
#     qury(second_string)
#     # Process the second string and generate the result
#     result = second_string.lower()  # Example: Convert the string to lowercase
#     print(result)
#     return jsonify({'second_string': result})

# app.run()

# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from pyngrok import ngrok

# app = Flask(__name__)
# CORS(app)

# # Route 1
# @app.route('/route1', methods=['POST'])
# def route1():
#     data = request.get_json()
#     text = data['text']
#     # Process the text and return a response
#     response = "Processed: " + text
#     return jsonify({'result': response})

# # Route 2
# @app.route('/route2', methods=['POST'])
# def route2():
#     data = request.get_json()
#     text = data['text']
#     # Process the text and return a response
#     response = "Processed: " + text
#     return jsonify({'result': response})

# # Start the tunnel
# public_url = ngrok.connect(addr="5000")
# print("Tunnel URL:", public_url)

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(port=5000)