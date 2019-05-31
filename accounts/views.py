from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup_view(request):
	if(request.method == 'POST'):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save() # returns the name of the user itself so need to retrieve separately
			login(request,user)
			return redirect('articles:list')
	else:
		form = UserCreationForm()
	return render(request,'accounts/signup_view.html',{'form':form})

def login_view(request):
	if(request.method == 'POST'):
		form = AuthenticationForm(data=request.POST) # need to assign to a variable data to get the login details
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('articles:list')

	else:
		form = AuthenticationForm()
	return render(request,'accounts/login_view.html',{'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('articles:list')