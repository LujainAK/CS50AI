# PageRank - CS50AI PageRank Algorithm Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project is a demonstration of what is used in search engines like Google to show the results in order of the **importance** and **quality**, which what we call here the **"PageRank"**. The code is calculating the **PageRank** for each page using two approaches: 
1. Sampling pages from a Markov Chain random surfer.
2. Iterative Algorithm: using the PageRank formula:

    <img src="PageRankFormula.png" width=40% height=50%>

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/tRnOn1wDuZ4).

## Installation
Download the file `pagerank.py`, and the directories `corpus0`, `corpus1`, and `corpus2`. Make sure they are all in the same directory named `pagerank`.

## Credits
The functions `transition_model`, `sample_pagerank`, and `iterate_pagerank` were implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 

The formula's image is taken from the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/).