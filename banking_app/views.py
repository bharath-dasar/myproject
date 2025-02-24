from django.shortcuts import render, redirect
from banking_app.models import UserProfile, Deposit, Loan, Repayment
from django.contrib.auth.decorators import login_required
from decimal import Decimal


@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    loans = Loan.objects.filter(borrower=profile)
    repayments = Repayment.objects.filter(loan__borrower=profile)

    return render(request, 'dashboard.html', {
        'profile': profile,
        'loans': loans,
        'repayments': repayments
    })


@login_required
def deposit(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        profile = UserProfile.objects.get(user=request.user)
        Deposit.objects.create(user=profile, amount=amount)
        profile.balance += Decimal(amount)
        profile.save()
        return redirect('dashboard')

    return render(request, 'deposit.html')


@login_required
def loan_request(request):
    if request.method == "POST":
        amount = float(request.POST.get('amount'))
        interest_rate = 10  # Example: Fixed 10% interest
        total_due = amount * 1.10
        profile = UserProfile.objects.get(user=request.user)

        Loan.objects.create(borrower=profile, amount=amount, interest_rate=interest_rate, total_due=total_due)
        return redirect('dashboard')

    return render(request, 'loan_request.html')


@login_required
def repayment(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        loan_id = request.POST.get('loan_id')  # Get selected loan
        amount_paid = Decimal(request.POST.get('amount_paid'))  # Get repayment amount

        loan = Loan.objects.get(id=loan_id, borrower=user_profile)  # Ensure loan belongs to user

        loan.total_due -= amount_paid
        if loan.total_due <= 0:
            loan.status = "PAID"
        loan.save()

        Repayment.objects.create(loan=loan, amount_paid=amount_paid)

        return redirect('dashboard')

    loans = Loan.objects.filter(borrower=user_profile, status="PENDING")
    return render(request, 'repayment.html', {'loans': loans})