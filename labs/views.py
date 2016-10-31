# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from labs.models import Result, Lab
from labs.forms import SubmitResultForm


@method_decorator(login_required(login_url='login'), name='dispatch')
class SubmitLab(CreateView):
    model = Result
    form_class = SubmitResultForm

    def get_success_url(self):
        return reverse('view_lab', kwargs={'lab_id': self.kwargs['lab_id']})

    def form_valid(self, form):
        form.instance.lab_id = self.kwargs['lab_id']
        form.instance.student = self.request.user
        return super(SubmitLab, self).form_valid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class ViewLab(ListView):
    model = Result
    paginate_by = 100

    def get_context_data(self, **kwargs):
        return super(ViewLab, self).get_context_data(
            lab=Lab.objects.get(id=self.kwargs['lab_id']), **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(student=self.request.user)
