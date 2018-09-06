from django.contrib import admin

from .models import Mineral, Group, Category


class MineralInline(admin.StackedInline):
    model = Mineral


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        MineralInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MineralInline,
    ]


admin.site.register(Mineral)
admin.site.register(Category, GroupAdmin)
admin.site.register(Group, GroupAdmin)
