from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import LoanAccount
from .forms import SignupForm, LoginForm, LoanForm # Assuming you have these forms
from django.shortcuts import render, redirect, get_object_or_404


def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save() 
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Ensure the field matches the form
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('loan')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username and password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def loan(request):
    return render(request, 'loan.html')

def loan_form_view(request):
    if request.method == "POST":  # Check if form is submitted
        form = LoanForm(request.POST)  # Get form data from request
        if form.is_valid():  # Validate form data
            loan = form.save(commit=False)  # Don't save yet
            loan.user = request.user  # Assign the logged-in user
            loan.status = "Pending"  # Set default status
            loan.save()  # Now save it
            return redirect('thankyou')  # Redirect after saving
    else:
        form = LoanForm()  # Create an empty form for GET request
    return render(request, 'loan_form.html', {'form': form})  # Pass form to template

def transactions(request):
    user_loans = LoanAccount.objects.filter(user=request.user)  # Fetch only the user's loans
    return render(request, 'transactions.html', {'loans': user_loans})

def pending_loans(request):
    loans = LoanAccount.objects.filter(user=request.user, status="Pending")
    return render(request, 'pending.html', {'loans': loans})
    
def approved(request):
    print(request.user,"riddhi")
    approved_loans = LoanAccount.objects.filter(user=request.user, status="Approved")

    return render(request, 'approved.html', {'loans': approved_loans})

def rejected(request):
    rejected_loans = LoanAccount.objects.filter(user=request.user, status="Rejected")
    return render(request, 'rejected.html', {'loans': rejected_loans})


def approve_loan(request, loan_id):
    print(loan_id,"riddhi")
    loan = get_object_or_404(LoanAccount, id=loan_id)
    loan.status = "Approved"  # Update status
    loan.save()
    return redirect('pending')  # Refresh the pending page

def reject_loan(request, loan_id):
    loan = get_object_or_404(LoanAccount, id=loan_id)
    loan.status = "Rejected"  # Update status
    loan.save()
    return redirect('pending')  # Refresh the pending page

def thankyou(request):
    return render(request, 'thankyou.html')
