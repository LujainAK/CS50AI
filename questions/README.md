# Questions - CS50AI Natural Language Processing Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project aims to build an AI that answers English questions about specific topics (documents) given in the directory `corpus` using **Natural Language Processing** tools.

* To rank the **documents** in order of their relevance to the question, the **tf-idf (Term Frequency - Inverse Document Frequency)** algorithm has been used.
* To rank the **sentences** in order of their relevance to the question, a combination of **idf (Inverse Document Frequency)** and **qtd (Query Term Density)** algorithms have been used.

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/6/questions/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/fENOof1ViMU).

## Installation
1. Download the files `questions.py`, and `requirements.txt`, as well as the directory of the documents `corpus`. Make sure they are all in the same directory named `questions`.
2. Install the package `nltk` which stands for **Natural Language Tool Kit**, by getting inside the directory `questions` and run
```bash
pip3 install -r requirements.txt
```

## Credits
The functions `load_files`, `tokenize`, `compute_idfs`, `top_files`, and `top_sentences` were implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 