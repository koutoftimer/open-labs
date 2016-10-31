# -*- encoding: utf-8 -*-
from django.db import models


class Lab(models.Model):
    title = models.CharField(max_length=256, default='', blank=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey('personnel.User')

    def __str__(self):
        return self.title


class DefinitionAttachment(models.Model):
    file = models.FileField(upload_to='lab-definitions')
    lab = models.ForeignKey(Lab, related_name='attachments')


class Result(models.Model):
    file = models.FileField(upload_to='lab-results')
    lab = models.ForeignKey(Lab)
    student = models.ForeignKey('personnel.User')
