from django.shortcuts import render
from home.models import News


# Create your views here.
def Home(request):
    news_model=News.objects.all().order_by('-date')
    context={"data":news_model}
    return render(request,"Home.html",context)

def Politics(request):
    news_model=News.objects.filter(category="politics").order_by('-date')
    context={"data":news_model}
    return render(request,"Politics.html",context)
def Sports(request):
    news_model=News.objects.filter(category="sports").order_by('-date')
    context={"data":news_model}
    return render(request,"Sports.html",context)
def Entertainment(request):
    news_model=News.objects.filter(category="entertainment").order_by('-date')
    context={"data":news_model}
    return render(request,"Entertainment.html",context)
def Currentaffair(request):
    news_model=News.objects.filter(category="currentaffair").order_by('-date')
    context={"data":news_model}
    return render(request,"Currentaffair.html",context)

