# Libraries
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import itertools
import os

import seaborn as sns
def loginpage(request):
	return render(request,'ded.html')
