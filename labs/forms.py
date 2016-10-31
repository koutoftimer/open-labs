# -*- encoding: utf-8 -*-
from django.forms import ModelForm

from labs.models import Result


class SubmitResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['file']
