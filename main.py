import scrapsplitvec
import chain
import query

retriever = SSV()
qa_chain_instrucEmbed = MDL(retriever = retriever)
Query("hello")