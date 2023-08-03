# Shopping - CS50AI K-Nearest-Neighbor Supervised Learning Classifier Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. Given a database about an online store customers (users), the project will build a K-Nearest-Neighbor Supervised Learning Classifier (KNN) that predicts whether the users will make a purchase by the end of their session. 

The accuracy in this project is in the form of two measures: 
1. Sensitivity (True Positive Rate): the proportion of positive examples that were correctly identified.
2. specificity (True Negative Rate): the proportion of negative examples that were correctly identified

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/4/shopping/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/o_xYoGgfP84).

## Installation
1. Download the file `shopping.py`, and the database `shopping.csv`. Make sure they are all in the same directory named `shopping`.
2. Install the package `scikit-learn` by running
```bash
pip3 install scikit-learn
```

## Credits
The functions `load_data`, `train_model`, and `evaluate` were implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 