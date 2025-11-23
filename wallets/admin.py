from django.contrib import admin


class WalletsAdmin(admin.ModelAdmin):
    list_display = "__all__"
