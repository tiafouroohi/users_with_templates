from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    all_users = User.objects.all()
    for user in all_users:
        print(user.first_name)
    context = {
        "all_users": all_users
    }
    return render(request, "index.html", context)

def process(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    age = request.POST['age']
    print({first_name}, {last_name}, {email}, {age})
    return redirect("/")


    







# Create your views here.
