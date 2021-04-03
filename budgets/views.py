from rest_framework import viewsets, permissions

from budgets.models import (
    Budget,
    Category,
    Entry
)
from budgets.serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print("DUPA")
        # self.request.user
        return Budget.objects.all()
