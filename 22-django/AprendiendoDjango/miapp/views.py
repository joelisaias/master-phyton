from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''
    <h1>Inicio</h1>
    ''')
def hola_mundo(request):
    return HttpResponse("<h1>Hola nundo desde DJango</h1>")