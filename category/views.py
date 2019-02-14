from django.shortcuts import render
from .models import categories

# Create your views here.
def index_view(request):
    categoryList = categories.objects.all()
    return render(request,"category/categories.html",{"categories":categoryList})

def category_detail(request,slug):
    categoryList = categories.objects.all()
    category = categories.objects.get(slug=slug)
    return render(request,"category/categories.html",{"categories":categoryList,"category":category})