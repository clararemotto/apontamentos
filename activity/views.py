from django.shortcuts import render

def index(request):
    return render(request, 'activity/index.html')

def add_activity(request):
    return render(request, 'activity/add_activity.html')
