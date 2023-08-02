from setuptools import setup, find_packages

setup(
    name='langBOTs',
    version='0.1.0',
    author='Rajat S',
    description='Scrape, Langchain, Deploy !',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires here
        'langchain',
        'tiktoken',
        'sentence_transformers',
        'InstructorEmbedding',
        'faiss-cpu',
        'unstructured',
        'flask',
        'pyngrtok',
        'flask-cors',
        'pydantic',
    ],
)
