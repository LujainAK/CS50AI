# Minesweeper - CS50AI Propositional Logic Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project aims to build a knowledge-based AI agent that plays and hopefully wins the **"Minesweeper"** puzzle game by making decisions according to its knowledge base and making inferences about it.

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/nqz5jjCgGUk).

## Installation
1. Download the files `runner.py`, `minesweeper.py`, and `requirements.txt` as well as the directory `assets`. Make sure they are all in the same directory named `minesweeper`.
2. Install the package `pygame` by getting inside the directory `minesweeper` and run
```bash
pip3 install -r requirements.txt
```

## Credits
The functions `known_mines`, `known_safes`, `mark_mine`, and `mark_safe` in `Sentence` class, and the functions `add_knowledge`, `make_safe_move`, and `make_random_movewere` in `MinesweeperAI` class were all implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 