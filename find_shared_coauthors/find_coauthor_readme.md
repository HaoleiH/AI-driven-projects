# known issues and future plan

1. I noticed that this code do not consider the case when the two people are coauthors to each other. This is easy to fix, but I still don;t have a good plan on how to show this relation, maybe use a thicker line to connect?
2. Google scholar does not have a official api so I have to use a third party api from [scholarly](https://github.com/scholarly-python-package/scholarly), which is not updated 2 years ago. This is the reason why the co-authors are not complete sometimes. A possible way to address this issue is to do the scraping by myself. I noticed that there is a interesting tool called [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai). It describe itself as this:
```
ScrapeGraphAI is a web scraping python library that uses LLM and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.).

Just say which information you want to extract and the library will do it for you!
```
May want to try that in the future.


# Here is a longer demo

[video](https://github.com/user-attachments/assets/a1b2596c-767b-4b1f-9361-69eb4bd6a131)




