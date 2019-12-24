from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import News
from .forms import NewsForm        


def get_news_list(request):
    news = News.objects.order_by('-published_date')
    return render(request, "news/news_list.html", {"news" : news})


def create_news(request):
    
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    if request.method == "POST":
        
        form = NewsForm(request.POST, request.FILES)
        
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_list')

    else:

        form = NewsForm()
        
    return render(request, 'news/news_form.html', {'form': form})


def news_details(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, "news/news_details.html", {'news': news})

    
def edit_news(request, pk):
   
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    news = get_object_or_404(News, pk=pk)
    newsId = pk
    
    if request.method == "POST":
        
        form = NewsForm(request.POST, request.FILES, instance=news)
        
        if form.is_valid():
            news = form.save()
            return redirect('news_details', news.pk)
            
    else:
         form = NewsForm(instance=news)
         edit = "True"
    
    return render(request, 'news/news_form.html', {'form': form, 'newsId':newsId, 'edit':edit})


def delete_news(request, pk):
   
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    news = get_object_or_404(News, pk=pk)
    news.delete()
    
    return redirect('news_list')
