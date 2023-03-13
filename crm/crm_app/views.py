from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record

def home(request):
    # Get all records in the table, assign to records variable.
    # Pass into the home page context if user is already logged in.
    records = Record.objects.all()

    # Check if user logging in, or already logged in
    # If logging in, POST req. If logged in, GET req.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate with django
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('home')
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate & login the new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Welcome. You have Registered Successfully")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    # Check if user is logged in
    if request.user.is_authenticated:
        # Look up record, pass record with matching id to variable
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.error(request, "You Must Be Logged In")
        return redirect('home')
        
def delete_record(request, pk):
    # Check if user is logged in
    if request.user.is_authenticated:
        # Look up record, pass record with matching id to variable
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.error(request, "Customer Record Deleted Successfully")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    # Check if user is logged in
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Customer Record Added Successfully")
                return redirect('home')
        # If request is not a POST request, then the user intends to fill the form.
        # Render the form and pass in the form to the page context, and return the same page
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In")
        return redirect('home')

def update_record(request, pk):
    # Check if user is logged in
    if request.user.is_authenticated:
        # Look up record, pass record with matching id to variable
        current_record = Record.objects.get(id=pk)
        # When the update page is accessed, the form should already be populated.
        # This is done by using an instance of the above variable, and passing it back into the page.
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Record Updated Successfully")
            return redirect('home')
        # If request is not a POST request, then the user intends to fill the form.
        # Render the form and pass in the form to the page context, and return the same page
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In")
        return redirect('home')