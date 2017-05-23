from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = HttpResponse()
    response.write("Rango says hello world!")
    response.write("<br><p><a href='about'>About </a></p>")
    return response


def about(request):
    response = HttpResponse()
    response.write("Here is the about page.")
    response.write("<br><p><a href='../'>Home </a></p>")
    response.write("<br><p><a href='/rango/'>Index</a></p>")
    return response
