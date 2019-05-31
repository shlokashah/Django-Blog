from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def article_list(request):
	articles=Articles.objects.all().order_by('date')
	return render(request,'articles/article_list.html',{'articles':articles})

def article_details(request,slug):
	article = Articles.objects.get(slug = slug)
	return render(request,'articles/article_details.html',{'article':article})

@login_required(login_url="/accounts/login/")
def create_article(request):
	return render(request,'articles/create_article.html')