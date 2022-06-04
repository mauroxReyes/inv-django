from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#ejemplo respose
def welcome(request):
	return render(request,"template/home.html",{})