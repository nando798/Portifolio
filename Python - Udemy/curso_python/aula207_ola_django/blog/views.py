from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def blog(request):
    print("Blog Page Requested")
    context ={
        "text": "Estamos no Blog",
        "title": "Blog - "
    }
    return render(request, "home/index.html",
context)

def example(request):
    print("Example Page Requested")
    context ={
        "text": "Estamos no Example",
        "title": "Example - "
    }
    return render(request, "home/index.html",
context)