# -*- encoding: utf-8 -*-
from django.contrib import admin

from personnel.models import Group, User


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Group, GroupModelAdmin)
admin.site.register(User)
