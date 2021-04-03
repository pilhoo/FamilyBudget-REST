from rest_framework import serializers

from budgets.models import (
    Budget,
    Category,
    Entry
)


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = ['name', 'entries', 'categories']


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['url', 'name']
