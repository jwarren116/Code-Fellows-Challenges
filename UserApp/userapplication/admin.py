from django.contrib import admin
from userapplication.models import UserDetail

class UserAdmin(admin.ModelAdmin):
    fields = ['fname', 'lname', 'email']
    list_display = ('id', 'fname', 'lname', 'email',)

admin.site.register(UserDetail, UserAdmin)