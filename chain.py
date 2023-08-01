from langchain import HuggingFacePipeline
from langchain.chains import RetrievalQA


class MDL:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.retriever
        # downloading model
        self.model_id = "bigscience/bloom-560m"
        self.task = "text-generation"
        self.model_kwargs = {"temperature": 0, "max_length": 512}
        self.device = 0
        self.llm = HuggingFacePipeline.from_model_id(model_id = self.model_id,task = self.task,model_kwargs = self.model_kwargs,device = self.device,)
        qa_chain_instrucEmbed = self.chain()
        return qa_chain_instrucEmbed

    #initialising chains
    def chain(self):
        qa_chain_instrucEmbed = RetrievalQA.from_chain_type(llm=self.llm,
                                                    chain_type="stuff",
                                                    retriever=self.retriever,
                                                    return_source_documents=True)
        return qa_chain_instrucEmbed                                            



