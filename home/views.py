from django.shortcuts import render
from home.models import News
from django.db.models import Q


# Create your views here.
def Home(request):

    news_model=News.objects.all().order_by('-date')
    if request.GET.get("search"):
         news_model = news_model.filter(
        Q(headline__icontains=request.GET.get("search")) | Q(description__icontains=request.GET.get("search"))
    )

    context={"data":news_model}
   

    return render(request,"Home.html",context)

def Politics(request):
    news_model=News.objects.filter(category="politics").order_by('-date')
    if request.GET.get("search"):
         news_model = news_model.filter(
        Q(headline__icontains=request.GET.get("search")) | Q(description__icontains=request.GET.get("search"))
    )
    context={"data":news_model}
    return render(request,"Politics.html",context)
def Sports(request):
    news_model=News.objects.filter(category="sports").order_by('-date')
    if request.GET.get("search"):
         news_model = news_model.filter(
        Q(headline__icontains=request.GET.get("search")) | Q(description__icontains=request.GET.get("search"))
    )
    context={"data":news_model}
    return render(request,"Sports.html",context)
def Entertainment(request):
    news_model=News.objects.filter(category="entertainment").order_by('-date')
    if request.GET.get("search"):
         news_model = news_model.filter(
        Q(headline__icontains=request.GET.get("search")) | Q(description__icontains=request.GET.get("search"))
    )
    context={"data":news_model}
    return render(request,"Entertainment.html",context)
def Currentaffair(request):

    news_model=News.objects.filter(category="currentaffair").order_by('-date')
    if request.GET.get("search"):
         news_model = news_model.filter(
        Q(headline__icontains=request.GET.get("search")) | Q(description__icontains=request.GET.get("search"))
    )
    context={"data":news_model}
    return render(request,"Currentaffair.html",context)
def read(request,pk):
      news_model=News.objects.get(id=pk)
      context={"data":news_model}
      return render(request,"fullnews.html",context)


