# AI-driven-projects
This repo contains some codes writen with the help of large language models like ChatGPT and Qwen.

## Find shared co-authors
[![open in Kaggle](https://img.shields.io/badge/open_in_Kaggle-blue?style=flat&logo=kaggle)](https://www.kaggle.com/code/haoleihui/find-coauthor)

[This file](./find_shared_coauthors/find-coauthor.ipynb) shows one example to visualize the relations between two scientist by using google scholar data obtained by [scholarly](https://pypi.org/project/scholarly/). The graph is made by streamlit and streamli-agraph. The code is mainly writen with the help of chatgpt. I made a little modification on it to make it fit my expectation, which in principle could also be done by using proper prompt. Following prompt is used:

```
create a web app by streamlit, user will input two names, use scholarly to find coauthor of the two names, use proxy to avoid getting banned, create flowchart by streamlit-agraph to show the connection between the two names and  their coauthors, if they share same coauthors, show them in a different color in the flowchart
```

Here is a video example.

[video](https://github.com/user-attachments/assets/2ed4e54b-bf2d-4082-8739-bf10050a83d8)



## RAG using Llama3.2-3b

[![hfspace](https://img.shields.io/badge/🤗-Space%20demo-yellow)](https://huggingface.co/spaces/holyhigh666/RAG-chalcogenide-perovskite) 
[![open in Kaggle](https://img.shields.io/badge/open_in_Kaggle-blue?style=flat&logo=kaggle)](https://www.kaggle.com/code/haoleihui/huggingface-website-successful)

Use Retrieval-Augmented Generation of large language models to build a chatbot, so that it can answer questions in specific field based on papers provided.

Details in [README_RAG.md](./RAG-using-Llama3.2-3b/README_RAG.md)

## data extraction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HaoleiH/AI-driven-projects/blob/main/data_extraction/Gemini_interface.ipynb)

Using google's Gemini to extract data from scientific papers. also tried llama 3.2 vision, ChatGPT, google deplot. not as good as gemini. click button above to run in colab. Check [this](./data_extraction/readme_data-extraction.md) to see an example.

This is one of the foundational components of a scientific Retrieval-Augmented Generation (RAG) large language model(LLM). The ultimate goal is to create a system similar to Google’s [NotebookLM](https://notebooklm.google.com/), enhanced with graph processing capabilities. This system would allow you to ask questions and receive answers from large language models based on the papers you provide.


## MinerU to convert pdf to markdown

[![Open in Kaggle](https://img.shields.io/badge/open_in_Kaggle-blue?style=flat&logo=kaggle)](https://www.kaggle.com/code/haoleihui/mineru-test)

Hosting a notebook in kaggle to convert scientific papers from human-readable pdf files to machine-readable markdown files by using [MinerU](https://github.com/opendatalab/MinerU). Kaggle provides resources like free CPU and 30 hours GPU per week so it is good for testing and sharing. One example of conversion is shown in [kaggle-MinerU](./kaggle-MinerU/test1.md). Now the notebook is purely running on CPU fore testing and is a little slow. The GPU acceleration will be added in the furture. Or you can check MinerU's official [documentation](https://github.com/opendatalab/MinerU?tab=readme-ov-file#using-gpu) if you want to develop your own code to enable GPU acceleration.

This is also one of the foundational components of a scientific Retrieval-Augmented Generation (RAG) large language model(LLM). The ultimate goal is to create a system similar to Google’s [NotebookLM](https://notebooklm.google.com/), enhanced with graph processing capabilities. This system would allow you to ask questions and receive answers from large language models based on the papers you provide.

## ocr translate 
see [this](https://github.com/HaoleiH/ocr_test). this is the first project I started with AI assisted programing.

## read plot
see [this](https://github.com/HaoleiH/read_plot). this is the second project. it is also hosted at [github pages](https://haoleih.github.io/HaoleiHui/readplot/read_plot.html) so that people can directly open this website and use it.

## dino game
this folder contains the programs to implement a chrome offline dino game. the most successful version is dino_qwen2.py. I also tried to make a script to automatically detect obstacles and jump to reach high score, but didn't finish it.

A screenshot of the dino game is shown here. ![dino game](./dino_game/screenshot.png)

## snake game
this folder contains code to build a snake game. a screen shot is shown here ![snake game](./snake_game/screenshot_snake.png)

## markdown rendering
this html file convert markdown to html or pdf. render_markdown_final.html is the final usable file and it is hosted [here](https://haoleih.github.io/HaoleiHui/manual/render_markdown.html). known issue is that it won't render equations like this $e^{i\pi}+1 = 0$.








