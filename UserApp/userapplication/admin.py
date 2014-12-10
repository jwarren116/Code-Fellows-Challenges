from django.contrib import admin
from userapplication.models import UserInfo

class UserAdmin(admin.ModelAdmin):
    fields = ['fname', 'lname', 'email']

admin.site.register(UserInfo, UserAdmin)