from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=100, blank=False, defualt='New Budget')
    privileges = models.ManyToManyField(User, related_name='budgets', through='Privilege')


class Privilege(models.Model):
    PRIVILEGES = (
        ('O', 'Owner'),
        ('E', 'Editor'),
        ('R', 'Read-only')
    )
    user = models.ForeignKey(User)
    budget = models.ForeignKey(Budget)
    privilege = models.CharField(max_length=1, choices=PRIVILEGES)


class Category(models.Model):
    budget = models.ForeignKey(Budget)
    name = models.CharField(max_length=100)


class Entry(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    budget = models.ForeignKey(Budget)
    category = models.ForeignKey(Category, blank=True)
