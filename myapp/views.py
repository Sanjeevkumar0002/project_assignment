from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.http import Http404


def hello(request):
    template = loader.get_template("hello.html")
    return HttpResponse(template.render())

def users(request):
    user = User.objects.all()
    return render(request, 'users.html',{"users": user})

def new_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        User.objects.create(name=name, email=email, role=role)
        return redirect('users')
    return render(request, 'new_user.html')


def user_detail(request, id):
    try:
        print(f"Fetching user with id: {id}")
        # This will raise Http404 if the user doesn't exist
        user = get_object_or_404(User, id=id)  
        return render(request, 'user_detail.html', {'user': user})  
    
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})
    
