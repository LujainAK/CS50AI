# Traffic - CS50AI Neural Network Project
The project is part of the [CS50AI](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) online course by Harvard University. This project aims to build a Convolutional Neural Network (CNN) using TensorFlow in Python to classify 43 different traffic signs based on images of these signs obtained from the [German Traffic Sign Recognition Benchmark (GTSRP)](https://benchmark.ini.rub.de/?section=gtsrb&subsection=news) dataset. 

All the background and specification details are on the exercise's page [HERE](https://cs50.harvard.edu/ai/2020/projects/5/traffic/). 

## Demo
A YouTube video to show the functionality demonstration of the project: [Click Here](https://youtu.be/c4EqO71kbpI).

## Experimentation Process
### Convolutional Layers
The Neural Network was built starting with 3 Convolutional Layers, each followed by a Maxpooling Layer with Pool Size (2,2). 
* The first convolutional layer has 32 filters that capture **Low-Level** features such as edges and corners. 
* The second convolutional layer has 64 filters that capture **Mid-Level** features such as texture and shapes.
* The third convolutional layer has 128 filters that capture **High-Level** features such as objects. 

This number of filters achieved an accuracy of 97.29% with a loss of 11.89%, which is acceptable given the complexity of the project.

The activation function used is `relu` to capture non-linear patterns which increases the efficiency. 

### Maxpooling Layers
There is a Maxpooling layer after each of the 3 convolutional layers. Maxpooling layers are used to reduce the size of the input by a factor of 2. This helps to generalize the learning process, reduce the computational cost, and eliminate noise in the images. The output of each maxpooling layer is an image with fewer pixels but more informative features.

### Flattening Layer
The flattening layer is used to convert the 3D features into 1D, to prepare it for the fully connected layers.

### Fully Connected Hidden Layers
The neural network has 2 dense hidden layers. These layers use the activation function `relu` to learn more complex and non-linear mapping, which improves the accuracy in general.

### Dropout Layer
The neural network drops out half of the units to assure generalization and prevent overfitting.

### The Output Layer
A dense layer is added to the neural network with `NUM_CATEGORIES` = 43 units to represent the output of each of the road signs in the dataset. The activation function here is `softmax` to ensure that the probabilities of all the final units are a sum up to 1 and they are all non-negative numbers. 

## Installation
1. Download the files `traffic.py`, and `requirements.txt`, as well as the directory of the dataset `gtsrb`. Make sure they are all in the same directory named `traffic`.
2. To install this project’s dependencies: opencv-python for image processing, scikit-learn for ML-related functions, and TensorFlow for neural networks. You need to go inside the traffic directory and run
```bash
pip3 install -r requirements.txt
```

## Credits
The functions `load_data` and `get_model` were implemented by Lujain Alkhelb. Everything else was implemented by the CS50AI course staff. 