# LangBOTs


A silly library which combines scraping, langchain and flask.
Inspired by [prompt engineering](https://www.youtube.com/@engineerprompt)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.


```bash
pip install langBOTs
```

## Usage

Default scrapes from example.com

```python 
from langBOTs.scrapsplitvec import SSV
from langBOTs.query import Query
from langBOTs.chain import MDL

retriever = SSV(chunk_size = 400, chunk_overlap = 100)
ret = retriever.ret()

chain = MDL(retriever = ret, device = 0).chain()

Q = Query(chain=chain)
Q.qury("hello how are you")
```
API
*Note: Requires [ngrok](https://ngrok.com/) token for tunneling.*

>$ ngrok config add-authtoken \<enter auth-token\>

also make sure you have flask pyngrok flask_ngrok flask_cors (1 of them is not rquired ig)

```python
from langBOTs.query import API
from langBOTs.query import process_second_string
from langBOTs.query import start

r = API(qury_object="Q") 
start(r)

```
I will post details on how to change the model and other aprameters soon.

## Flow

(scrape->load->split->[dwnld_instructor_e]->create_vec_graph->save(optional)->[download_model->]initialise_chain->query->)->api

## Contributing

Yo

## License

[MIT](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## By
[Rajat](https://rajat.xyz)

