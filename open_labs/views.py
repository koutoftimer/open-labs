# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group as Role
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from registration.views import (
    RegistrationView as RegView, RegistrationForm as RegForm
)

from personnel.models import Group, User


@method_decorator(login_required(login_url='login'), name='dispatch')
class Home(TemplateView):
    template_name = 'open_labs/home.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'teacher': Role.objects.get(name='Teacher'),
            'student': Role.objects.get(name='Student'),
        })
        return kwargs


class RegistrationForm(RegForm):
    email = forms.EmailField(help_text='email address')
    role = forms.ModelChoiceField(queryset=Role.objects.all(),
                                  initial=Role.objects.get(name='Student'))
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta(RegForm.Meta):
        fields = [
            User.USERNAME_FIELD,
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class RegistrationView(RegView):
    form_class = RegistrationForm
    success_url = 'home'

    def form_valid(self, form: RegistrationForm):
        instance = form.save()
        instance = User.objects.get(id=instance.id)
        instance.groups.add(form.cleaned_data['role'])
        instance.group_set.add(form.cleaned_data['group'])
        return redirect(self.success_url)
