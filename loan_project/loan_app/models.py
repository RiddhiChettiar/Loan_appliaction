from django.db import models
from django.contrib.auth.models import User

class LoanAccount(models.Model):  
    LOAN_TYPE_CHOICES = [
        ('home', 'Home Loan'),
        ('car', 'Car Loan'),
        ('business', 'Business Loan'),
        ('personal', 'Personal Loan'),
        ('educational', 'Educational Loan'),
        ('other', 'Other'),
    ]

    INTEREST_RATE_CHOICES = [
        (5.0, '5%'),
        (7.0, '7%'),
        (10.0, '10%'),
        (12.0, '12%'),
        (15.0, '15%'),
    ]

    STATUS_CHOICES = [
    ('Pending','Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    reason = models.CharField(max_length=500, default="Not Specified")
    loan_type = models.CharField(max_length=20, default="Personal Loan")
    amount = models.BigIntegerField(default=30000)
    interest_rate = models.FloatField(default=5.0)
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f"{self.name} {self.surname}"
