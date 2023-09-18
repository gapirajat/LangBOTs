"""Calling langchain to predict aswell as doing some post processing"""
import textwrap
from pydantic import BaseModel
from typing import Any

class Query(BaseModel):
    chain: Any = None

    def wrap_text_preserve_newlines(self, text, width=110):
        # Split the input text into lines based on newline characters
        lines = text.split('\n')

        # Wrap each line individually
        wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

        # Join the wrapped lines back together using newline characters
        wrapped_text = '\n'.join(wrapped_lines)

        return wrapped_text

    def process_llm_response(self, llm_response):
        # print(self.wrap_text_preserve_newlines(llm_response['result']))
        print('\nResponse:')
        # for source in llm_response["source_documents"]:
        #     return source.metadata['source']
        return self.wrap_text_preserve_newlines(llm_response['result'])

    def qury(self, query: str):
        llm_response = self.chain(query)
        res = self.process_llm_response(llm_response)
        return res