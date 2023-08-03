# Nim - CS50AI Reinforcement Learning Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project aims to build an AI that learns by Q-Learning Reinforcement Learning how to play and win the game **"Nim"**. In the code, it was chosen to train the AI 10,000 times, so its performance is getting better over time. 

The Q-Learning formula used:

    `Q(s, a) <- Q(s, a) + alpha * (new value estimate - old value estimate)`

Where `alpha` is the learning rate, `new value estimate` is the sum of current and future rewards recieved, and `old value estimate` is the current `Q(s, a)`.

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/4/nim/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/DcbCflTA_JI).

## Installation
Download the files `nim.py`, and `play.py`. Make sure they are all in the same directory named `nim`.

## Credits
The functions `get_q_value`, `update_q_value`, `best_future_reward`, and `choose_action` in `nim.py` were implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 