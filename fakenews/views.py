# Libraries
from django.shortcuts import render
from django.http import HttpResponse
import os

def loginpage(request):
	return render(request,'ded.html')
