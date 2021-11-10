from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "this is the index view")

def room(request, room_name):
    return (request, {
        'room_name': room_name
    })