from django.db import models

TYPE_CHOICES = {
    ('Deposit','Deposit'),
    ('Withdrawal','Withdrawal'),
}

class Account(models.Model):
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Starting Balance = models.DecimalField(default=0.00, max_digits = 10000,decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name, self.Last_Name

class Transaction()
    Date_of_Transaction = models.DateField(auto_now=False, auto_now_add=False)
    Type_of_Transaction = models.CharField(max_length=60, choices=TYPE_CHOICES)
    Amount = models.DecimalField(default=0.00, max_digits = 10000,decimal_places=2)
    Description = models.TextField(max_length = 300, default="", blank=True)
    Account_it_applies_to = models.CharField(max_length=60, choices=TYPE_CHOICES)


    objects = models.Manager()

    def __str__(self):
        return self.Date_of_Transaction