from django.urls import path
from .views import Signup, login, loan, loan_form_view, transactions, pending_loans, approved, rejected, approve_loan, reject_loan, thankyou

urlpatterns = [
    path('', Signup, name='signup'),
    path('login/', login, name='login'),
    path('loan/', loan, name='loan'),
    path('loan_form/', loan_form_view, name='loan_form'),
    path('transactions/', transactions, name='transactions'),
    path('pending/', pending_loans, name='pending'),
    path('approved/', approved, name='approved'),
    path('rejected/', rejected, name='rejected'),
    path('approve/<int:loan_id>/', approve_loan, name='approve_loan'),
    path('reject/<int:loan_id>/', reject_loan, name='reject_loan'),
    path('thankyou/', thankyou, name='thankyou'),
]
