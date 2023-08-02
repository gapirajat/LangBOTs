from langchain import HuggingFacePipeline
from langchain.chains import RetrievalQA
import pydantic
from typing import Optional


class MDL:
    retriever: any
    model_id: str = "bigscience/bloom-560m"
    task: str = "text-generation"
    model_kwargs: dict = {"temperature": 0, "max_length": 512}
    # device: int = 0
    llm: any = HuggingFacePipeline.from_model_id(model_id, task, model_kwargs, device,)

    # def __init__(self, retriever, model_id = "bigscience/bloom-560m", task = "text-generation", model_kwargs = {"temperature": 0, "max_length": 512}, device = 0):
    #     self.retriever = retriever
    #     # downloading model
    #     self.model_id = model_id
    #     self.task = task
    #     self.model_kwargs = model_kwargs
    #     self.device = device
    #     self.llm = HuggingFacePipeline.from_model_id(model_id = self.model_id,task = self.task,model_kwargs = self.model_kwargs,device = self.device,)

    #initialising chains
    def chain(self):
        qa_chain_instrucEmbed = RetrievalQA.from_chain_type(llm=self.llm,
                                                    chain_type="stuff",
                                                    retriever=self.retriever,
                                                    return_source_documents=True)
        return qa_chain_instrucEmbed                                            


