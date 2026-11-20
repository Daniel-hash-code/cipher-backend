from django.contrib import admin
from .models import Contact, Employee

# Register models here.
# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ("full_name", "email", "subject", "created_at")

admin.site.register(Contact)
admin.site.register(Employee)