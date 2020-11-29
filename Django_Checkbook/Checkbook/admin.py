from django.contrib import admin

from .models import account

admin.site.register(Account)

from .models import transaction

admin.site.register(Transaction)
