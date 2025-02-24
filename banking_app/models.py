import time

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import date, timedelta

class UserProfile(models.Model):
    """
    Extends Django's built-in User model to add additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User
    phone = models.CharField(max_length=15, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username

class Account(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=[('SAVINGS', 'Savings'), ('CHECKING', 'Checking')])
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=now)  # Default value added

    def __str__(self):
        return f"{self.account_number} - {self.user.user.username}"

class Transaction(models.Model):
    """
    Tracks deposits, withdrawals, and transfers.
    """
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('TRANSFER', 'Transfer'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} by {self.account.user.user.username}"

class Deposit(models.Model):
    """
    Represents a user's deposit.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deposit: {self.amount} by {self.user.user.username}"

class Loan(models.Model):
    """
    Represents a loan taken by a user.
    """
    borrower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="loans")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()  # Percentage
    total_due = models.DecimalField(max_digits=10, decimal_places=2)  # Includes interest
    due_date = models.DateField(default=date.today() + timedelta(days=180))
    status = models.CharField(max_length=20, choices=[("PENDING", "Pending"), ("PAID", "Paid")], default="PENDING")

    def __str__(self):
        return f"Loan: {self.amount} to {self.borrower.user.username}"

class Repayment(models.Model):
    """
    Represents a repayment towards a loan.
    """
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repayment: {self.amount_paid} for {self.loan.borrower.user.username}"
