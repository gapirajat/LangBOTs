from setuptools import setup, find_packages

setup(
    name='langBOTs',
    version='0.0.32',
    author='Rajat S',
    description='Scrape, Langchain, Deploy !',
    url = 'https://github.com/gapirajat/langBOTs',
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
        # 'pyngrtok',
        'flask-cors',
        'pydantic',
    ],
     classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Scientific/Engineering :: Artificial Intelligence',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
