# -*- encoding: utf-8 -*-
from django.contrib import admin

from labs.models import Lab, DefinitionAttachment, Result


admin.site.register(Lab)
admin.site.register(DefinitionAttachment)
admin.site.register(Result)
