from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['book', 'member', 'issue_date', 'return_date', 'status']
    list_filter=['status', 'issue_date']
    search_fields=['book__title', 'member__name']
