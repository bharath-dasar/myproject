from django.contrib import admin
from .models import *

# admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(UserProfile)
admin.site.register(Deposit)
admin.site.register(Loan)
admin.site.register(Repayment)
