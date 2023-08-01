#(scrape->load->split->[dwnld_instructor_e]->create_vec_graph->save(optional)->[download_model->]initialise_chain->query->)->api
from langchain.document_loaders import UnstructuredURLLoader #to load the source text 
from langchain.text_splitter import CharacterTextSplitter #chunking the load data

import faiss#vector graph knowledge base
from langchain.vectorstores import FAISS

from InstructorEmbedding import INSTRUCTOR# InstructorEmbedding
from langchain.embeddings import HuggingFaceInstructEmbeddings

# Python code to illustrate the Modules
class SSV:

	def __init__(self):
		self.urls = ['https://it.pccoepune.com/','https://it.pccoepune.com/hod']
        self.chunk_size = 600
        self.chunk_overlap = 100
        self.model_name = "hkunlp/instructor-xl"
        self.kwargs = 3
        
        retriever = self.vec(self.split(self.scrap()))
        return retriever

	# A normal print function
	def scrap(self):
		loaders = UnstructuredURLLoader(urls=urls)
        data = loaders.load()
        return data

	def split(self, data):
        #initialised text splitter
        text_splitter = CharacterTextSplitter(separator=' ',
                                      chunk_size=self.chunk_size,
                                      chunk_overlap=self.chunk_overlap)
        #split the text                              
        docs = text_splitter.split_documents(data)                              
        return docs                              

	def vec(self, docs):
        #downloading instructor embedding
        instructor_embeddings = HuggingFaceInstructEmbeddings(model_name=self.model_name,
                                                      model_kwargs={"device": "cuda"})
        #creating vector graph
        db_instructEmbedd = FAISS.from_documents(docs, instructor_embeddings)
        retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": self.kwargs})
        return retriever
#urls, chunk size, overlap, search kwargrs, instructor model
