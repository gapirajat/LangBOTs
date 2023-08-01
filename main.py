import scrapsplitvec
import model
import query

retriever = SSV()
qa_chain_instrucEmbed = MDL(retriever = retriever)
Query("hello")