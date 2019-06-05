from django.shortcuts import render,redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.files.storage import FileSystemStorage
# Create your views here.

def article_list(request):
	articles=Articles.objects.all().order_by('date')
	return render(request,'articles/article_list.html',{'articles':articles})

def article_details(request,slug):
	article = Articles.objects.get(slug = slug)
	return render(request,'articles/article_details.html',{'article':article})

@login_required(login_url="/accounts/login/")
def create_article(request):
	if request.method == 'POST':
		form=forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
	else:
			form = forms.CreateArticle()
	return render(request,'articles/create_article.html',{'form':form})

@login_required(login_url="/accounts/login/")
def delete_article(request,pk):
	if request.method =='POST':
		article = Articles.objects.get(pk = pk)
		article.delete()
	return redirect('articles:list')

