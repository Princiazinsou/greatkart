from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'nom' ,'prenom', 'username', 'last_login', 'date_joined', 'is_active')

    list_display_links = ('email', 'nom', 'prenom')
    readonly_fields = ('last_login', 'date_joined')
    ordering= ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account , AccountAdmin)
