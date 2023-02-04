# Kitchenware Classifier by 🅱🅻🅰🆀
![kt](https://user-images.githubusercontent.com/100685852/216769983-16201e21-ce55-4625-a203-c85b5a7da132.jpg)

# Overview
This project contains a deep learning model that classifies kitchenware into one of six categories:
``` spoons```, 
```forks```,
``` glasses```, 
``` cups```, 
``` plates```, and 
``` knives```. 

The model was trained on a dataset of kitchenware images that can be gotten from [Kaggle](https://www.kaggle.com/competitions/kitchenware-classification/overview) and
can be used to recognize kitchenware in real-life scenarios. This classifier could be helpful to a store owner who wishes to take an inventory of the items that they 
have. This repo is an improvement on the previous one of this same project. I improved upon the accuracy from 93% to 96.5%, then I hosted the model to a web service
using flask, and later deployed to dockerhub.

# Requirements
The following libraries are required to run the code in this repository:
```TensorFlow```
```Keras```
```Numpy```
```requests```
```waitress```
```pillow```

# Usage

To use the model, you can run the predict.py file in your terminal:

```$ python predict.py```
then
```$ python predict_test.py```
in another window. The model will output the predicted class of the kitchenware in the image.



# Limitations
The model was trained on a limited dataset and may not perform well on images of kitchenware that are significantly different from the images in the training dataset.
Additionally, the model may not perform well on images that are taken from unusual angles or in poor lighting conditions.

# Future Work
Future work on this project could include:

Improving the performance of the model on a wider range of kitchenware images.
Incorporating additional kitchenware categories.



