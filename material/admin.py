from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city',)
    list_filter = ('email',)
    search_fields = ('email',)
