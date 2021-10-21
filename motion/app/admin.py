from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class MyUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'firstname', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()
    ordering = ('email',)

    add_fieldsets = (
    (None, {
            'classes':('wide',),
            'fields':('email','username', 'firstname','lastname','password1','password2')
        }
    ),  # <-- add this comma!
)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Package)
admin.site.register(List)
admin.site.register(Interest)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Error)
admin.site.register(Setting)
admin.site.register(Proof)
admin.site.register(Approved)
admin.site.register(Referral_reward)
admin.site.register(Dividens)
# Register your models here.
