# -*- encoding: utf-8 -*-
from django.contrib import admin

from labs.models import Lab, DefinitionAttachment, Result


class GroupsFilter(admin.SimpleListFilter):
    title = 'group name'
    parameter_name = 'group'

    def lookups(self, request, model_admin):
        groups = model_admin.get_queryset(request).values_list(
            'student__group__name', flat=True).distinct()
        return [(g, g) for g in groups]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(student__group__name=self.value())
        return queryset


class ResultModelAdmin(admin.ModelAdmin):
    list_filter = ('lab__title', 'student__last_name', GroupsFilter)
    list_display = ('lab_title', 'student_name', 'file')

    def get_actions(self, request):
        return []

    def get_queryset(self, request):
        return super(ResultModelAdmin, self).get_queryset(request).filter(
            student__groups__name='Student')

    def lab_title(self, obj: Result):
        return obj.lab.title

    lab_title.admin_order_field = 'lab__title'

    def student_name(self, obj: Result):
        return '{} {}'.format(obj.student.last_name, obj.student.first_name)

    student_name.admin_order_field = 'student__last_name'


class DefinitionAttachmentInline(admin.StackedInline):
    model = DefinitionAttachment


class LabModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_names')
    inlines = [DefinitionAttachmentInline]

    def group_names(self, obj: Lab):
        return ', '.join(obj.group_set.values_list('name', flat=True))


admin.site.register(Lab, LabModelAdmin)
admin.site.register(DefinitionAttachment)
admin.site.register(Result, ResultModelAdmin)
