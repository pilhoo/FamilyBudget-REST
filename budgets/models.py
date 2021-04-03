from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=100, blank=False, default='New Budget')
    privileges = models.ManyToManyField(User, related_name='budgets', through='Privilege')

    def __str__(self):
        return self.name


class Privilege(models.Model):
    PRIVILEGES = (
        ('O', 'Owner'),
        ('E', 'Editor'),
        ('R', 'Read-only')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, related_name='categories', on_delete=models.CASCADE)
    privilege = models.CharField(max_length=1, choices=PRIVILEGES)


class Category(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.budget.name})"

    class Meta:
        verbose_name_plural = "Categories"


class Entry(models.Model):
    CURRENCIES = (
        ('PLN', 'Polski Złoty'),
        ('EUR', 'Euro'),
        ('USD', 'American Dollar')
    )

    name = models.CharField(max_length=100, blank=False, default='')
    amount = models.FloatField(default=0.)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='PLN')
    budget = models.ForeignKey(Budget, related_name='entries', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.amount}{self.currency} ({self.budget.name})'\
               + (f' [{self.category.name}]' if self.category else '')

    class Meta:
        verbose_name_plural = "Entries"
