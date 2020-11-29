from django.forms import ModelForm
from.models import Product

class Account(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class Transaction(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'