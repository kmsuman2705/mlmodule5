#!/usr/bin/env python
# coding: utf-8

# In[5]:
pip install scikit-learn
from sklearn.linear_model import LogisticRegression



import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


# In[23]:


mind = joblib.load('Species_mind.pk1')
def predict_species():
    print("Enter the sepal length, sepal width, petal length, and petal width of the flower:")
    sepal_length = float(input("Sepal Length: "))
    sepal_width = float(input("Sepal Width: "))
    petal_length = float(input("Petal Length: "))
    petal_width = float(input("Petal Width: "))
    user_input = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Make predictions
    prediction = mind.predict(user_input)

    print("Predicted Species:", prediction[0])

# Test the function
predict_species()



# In[ ]:




