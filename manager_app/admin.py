from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager_app.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    list_filter = UserAdmin.list_filter + ("years_of_experience", )
    search_fields = UserAdmin.search_fields + (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title", "content", )
    list_display = ("title", "published_date", )
    list_filter = ("topics", "publishers", )
    raw_id_fields = ("publishers", )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", )
