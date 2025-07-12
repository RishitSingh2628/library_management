from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'membership_date', 'is_active']
    list_filter=['is_active', 'membership_date']
    search_fields=['name', 'email']
# Register your models here.
