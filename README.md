## LangBOTs

# Description

A silly library which combines scraping, langchain and flask.
Inspired by [prompt engineering](https://www.youtube.com/@engineerprompt)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
(scrape->load->split->[dwnld_instructor_e]->create_vec_graph->save(optional)->[download_model->]initialise_chain->query->)->api
```bash
pip install langBOTs
```

## Usage

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

## Contributing

Yo

## License

[MIT](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## By
[Rajat](https://rajat.xyz)

