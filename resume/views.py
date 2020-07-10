from django.shortcuts import render

# Create your views here. main app view.py
def home(request):
    return render(request,'resume.html')