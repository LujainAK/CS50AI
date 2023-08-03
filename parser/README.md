# Parser - CS50AI Context-Free Grammar - Natural Language Processing Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project aims to build an AI that parse English sentences and extract noun phrases using **Context-Free Grammar Rules** and **Natural Language Proccessing** tools.

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/6/parser/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/aFOXdJDV0u0).

## Installation
1. Download the files `parser.py`, and `requirements.txt`, as well as the directory of the sentences `sentences`. Make sure they are all in the same directory named `parser`.
2. Install the package `nltk` which stands for **Natural Language Tool Kit**, by getting inside the `parser` directory and run
```bash
pip3 install -r requirements.txt
```

## Credits
The functions `preprocess` and `np_chunk`, and the context-free grammar rules defined in `NONTERMINALS` were all implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 