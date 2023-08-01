#(scrape->load->split->[dwnld_instructor_e]->create_vec_graph->save(optional)->[download_model->]initialise_chain->query->)->api
from langchain.document_loaders import UnstructuredURLLoader #to load the source text 
from langchain.text_splitter import CharacterTextSplitter #chunking the load data
urls = [
    'https://it.pccoepune.com/',
    'https://it.pccoepune.com/hod'
]
loaders = UnstructuredURLLoader(urls=urls)
data = loaders.load()
#initialised text splitter
text_splitter = CharacterTextSplitter(separator=' ',
                                      chunk_size=600,
                                      chunk_overlap=100)

#split the text
docs = text_splitter.split_documents(data)

#first load then split
def process_data(urls):
    global loaders, data, db_instructEmbedd, retriever, text_splitter, docs, qa_chain_instrucEmbed

    #loading html to data
    loaders = UnstructuredURLLoader(urls=urls) 
    data = loaders.load()

    #initialising splitter
    text_splitter = CharacterTextSplitter(separator=' ',
                                          chunk_size=600,
                                          chunk_overlap=100)

    #splitting
    docs = text_splitter.split_documents(data)

    #downloading instructor embedding
    instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl",
                                                      model_kwargs={"device": "cuda"})

    #creating vector graph
    db_instructEmbedd = FAISS.from_documents(docs, instructor_embeddings)
    retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": 3})



    

    !pip install transformers > /dev/null
    from langchain import HuggingFacePipeline

    #downloading model
    llm = HuggingFacePipeline.from_model_id(
        model_id="bigscience/bloom-560m",
        task="text-gen",
        model_kwargs={"temperature": 0, "max_length": 512},
        device=0,
    )
    #initialising chains
    qa_chain_instrucEmbed = RetrievalQA.from_chain_type(llm=llm,
                                                       chain_type="stuff",
                                                       retriever=retriever,
                                                       return_source_documents=True)#initialising langchian pipeline


import pickle
import faiss
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
# InstructorEmbedding
from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings

## making vector graph emebdding

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl",
                                                      model_kwargs={"device": "cuda"})



db_instructEmbedd = FAISS.from_documents(docs, instructor_embeddings)
retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": 3})

#BLOOM LLM

# !pip install transformers > /dev/null
# from langchain import HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id="bigscience/bloom-560m",
#     task="text-generation",
#     model_kwargs={"temperature": 0, "max_length": 512},
#     device=0,
# )

#CHAIN

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain

#fn
# qa_chain_instrucEmbed = RetrievalQA.from_chain_type(llm=llm,
#                                   chain_type="stuff",
#                                   retriever=retriever,
#                                   return_source_documents=True)

import textwrap

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

def process_llm_response(llm_response):
    print(wrap_text_preserve_newlines(llm_response['result']))
    print('\nSources:')
    for source in llm_response["source_documents"]:
        return source.metadata['source']

def qury(query):
  print('-------------------Instructor Embeddings------------------\n')
  llm_response = qa_chain_instrucEmbed(query)
  res = process_llm_response(llm_response)
  return res

#API

from flask import Flask, request, jsonify

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install flask pyngrok
# from pyngrok import ngrok





!pip install flask-ngrok flask-cors

from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)

@app.route('/api/first_string', methods=['POST', 'OPTIONS'])
def process_first_string():
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
    first_string = data['first_string']
    process_data(first_string)

    # Process the first string and generate the result
    result = first_string.upper()  # Example: Convert the string to uppercase

    return jsonify({'first_string': result})

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
    qury(second_string)
    # Process the second string and generate the result
    result = second_string.lower()  # Example: Convert the string to lowercase
    print(result)
    return jsonify({'second_string': result})

app.run()

from flask import Flask, jsonify, request
from flask_cors import CORS
from pyngrok import ngrok

app = Flask(__name__)
CORS(app)

# Route 1
@app.route('/route1', methods=['POST'])
def route1():
    data = request.get_json()
    text = data['text']
    # Process the text and return a response
    response = "Processed: " + text
    return jsonify({'result': response})

# Route 2
@app.route('/route2', methods=['POST'])
def route2():
    data = request.get_json()
    text = data['text']
    # Process the text and return a response
    response = "Processed: " + text
    return jsonify({'result': response})

# Start the tunnel
public_url = ngrok.connect(addr="5000")
print("Tunnel URL:", public_url)

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)