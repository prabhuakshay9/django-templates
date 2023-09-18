from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from simple_history.admin import SimpleHistoryAdmin

from .models import CustomUser


class CustomUserAdmin(SimpleHistoryAdmin, UserAdmin):
    """
    Custom admin class for the CustomUser model,
    inheriting from SimpleHistoryAdmin and UserAdmin.
    """

    # Define the fields to be displayed in the list view of the admin panel.
    list_display = ("email", "name", "is_staff", "last_login")

    # Enable searching by email, first_name, and last_name in the admin panel.
    search_fields = ("email", "first_name", "last_name")

    # Add filters for is_staff, is_superuser, and groups in the admin panel.
    list_filter = ("is_staff", "is_superuser", "groups")

    # Organize the fields into sections within the detail view of a user.
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Define the fields for adding a new user.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_staff",
                "is_active"
            ),
        }),
    )

    # Define the default ordering of users in the admin panel.
    ordering = ("email",)

    # Enable managing groups and user permissions using horizontal filter widgets.
    filter_horizontal = ("groups", "user_permissions")

    # Display last_login and date_joined fields as read-only in the admin panel.
    readonly_fields = ("last_login", "date_joined")


# Register the CustomUser model and Permission model with their respective admins.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Permission)
