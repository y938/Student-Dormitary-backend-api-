from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [  
             
        "first_name",
        "last_name",
        "email",
        "department",
        "room",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                
                    "department",
                   
                    "year",
                    "block",
                    "room",
                    "bed",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    
                    "department",
                    
                    "year",
                    "block",
                    "room",
                    "bed",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)