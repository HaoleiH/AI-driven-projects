# RAG using Llama3.2-3b

[Open in Kaggle](https://www.kaggle.com/code/haoleihui/cp-rag-llms)
# How it works

[![theory](RAG_theory.png)](https://x.com/akshay_pachaar/status/1816088897505615925)
This graph show the major procedures in a RAG system. Most time consuming process is 3 -> 4 ->5. when you ask a question, the system need to search in a vector database to find related context, then pass the context together with the question to a large language model, combining with a prompt to tell it answering questions based on the context.
# Results
This folder contains the notebook I used in local computer for testing. The kaggle notebook is running on its free Nvidia P100 GPU.

Results of using pdf and markdown as input and shown below.

Markdown input
![md](RAG-md.PNG)

pdf input
![md](RAG-pdf.PNG)

# Future plans
Continuing from RAG with markdown input, we need to find a way to retrieve graph in input files.