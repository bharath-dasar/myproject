from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this!
    path('deposit/', views.deposit, name='deposit'),
    path('loan/', views.loan_request, name='loan_request'),
    path('repayment/', views.repayment, name='repayment'),
]
