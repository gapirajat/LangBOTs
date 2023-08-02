from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
import textwrap
import pydantic
from typing import Optional

class Query:
    chain: any
    
    def wrap_text_preserve_newlines(self, text, width=110):
        # Split the input text into lines based on newline characters
        print(type(text))
        lines = text.split('\n')

        # Wrap each line individually
        wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

        # Join the wrapped lines back together using newline characters
        wrapped_text = '\n'.join(wrapped_lines)

        return wrapped_text

    def process_llm_response(self, llm_response):
        print(self.wrap_text_preserve_newlines(llm_response['result']))
        print('\nSources:')
        for source in llm_response["source_documents"]:
            return source.metadata['source']

    def qury(self, query: str):
        print('-------------------Instructor Embeddings------------------\n')
        llm_response = self.chain(query)
        res = self.process_llm_response(llm_response)
        return res