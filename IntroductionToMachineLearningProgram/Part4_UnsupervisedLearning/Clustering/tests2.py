import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from IPython.display import Image
from sklearn.datasets import make_blobs

def display_gif(fn):
    return '<img src="{}">'.format(fn)


def test_question_1(data1):
    if data1.shape[0] == 200 and data1.shape[1] == 5:
        print("Looks good!  Continue!")
    else:
        print("Oops, that looks different than what we expected!  The first argument should be the number of rows, the second the number of columns, and the final should be the number of centers.")

def test_question_2(k_value):
    if k_value == 4:
        print("That's right!  The value of k is the same as the number of centroids used to create your dataset.")
    else:
        print("Oops! That doesn't seem right!  The value of k should be the same as the number of centroids you used in your dataset.  In this case, the value for k should be 4.")

def test_question_7(k_value):
    if k_value == 4:
        print("That's right!  We set up the data with 4 centers, and the plot is consistent!  We can see a strong leveling off after 4 clusters, which suggests 4 clusters should be used.")

        return display_gif("https://media2.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif")
    else:
        print("Oops! That doesn't seem right!  The value of k should be where the 'elbow' can be found in the scree plot.  You can see 4-10 all have similar SSE values, suggesting that 4 clusters is the minimum number of clusters to significantly reduce the SSE from centroids to each point.")

def check_q1(stuff):
    a = 0
    b = 60
    c = 22.9
    d = 4.53
    e = 511.7

    q1_dict = {
    'number of missing values': a,
    'the mean 5k time in minutes': c,    
    'the mean test score as a raw value': e,
    'number of individuals in the dataset': b
    }
    
    if stuff == q1_dict:
        print("That looks right!")
    
    else:
        print("Oops!  That doesn't look quite right! Try again.")
    
def check_q5(stuff):
    
    a = 'We should always use normalizing'
    b = 'We should always scale our variables between 0 and 1.'
    c = 'Variable scale will frequently influence your results, so it is important to standardize for all of these algorithms.'
    d = 'Scaling will not change the results of your output.'

    if stuff == c:
        return Image(filename="./giphy.gif")
    else:
        print("Oops!  That doesn't look quite right.  Try again!")
