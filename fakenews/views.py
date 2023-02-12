# Libraries
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import emoji
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import PassiveAggressiveClassifier
import os

import seaborn as sns
def loginpage(request):
	return render(request,'ded.html')
