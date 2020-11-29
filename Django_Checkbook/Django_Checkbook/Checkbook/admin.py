from django.contrib import admin


from .models import Account

admin.site.register(Account)

from .models import Transaction

admin.site.register(Transaction)
