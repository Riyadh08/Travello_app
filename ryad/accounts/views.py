from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):

    if request.method == 'POST':
    # Get the post parameters
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname)
        user.save()
        print('User created')
        return redirect('/')

    else:
        return render(request, 'register.html')