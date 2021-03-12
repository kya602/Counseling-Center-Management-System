from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Client,Questionnaire,AnxietyMeasure,Case_File,DepressionMeasure


# Define an inline admin descriptor for Client model
# which acts a bit like a singleton
'''
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''
