from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.middleware.csrf import get_token

def index(request):
    itemlist = User.objects.order_by('-date')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_site")
    else:
        form = UserForm()
    page = {
        "forms": form,
        "List": itemlist,
        "title": "TODO APP",
    }
    print (request.POST.get("itemlist"))
    return render(request, 'home.html')