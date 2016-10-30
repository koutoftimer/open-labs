# -*- encoding: utf-8 -*-
from django.db import models


class Lab(models.Model):
    title = models.CharField(max_length=256, default='', blank=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey('auth.User')


class DefinitionAttachment(models.Model):
    file = models.FileField(upload_to='lab-definitions')
    lab = models.ForeignKey(Lab)


class Result(models.Model):
    file = models.FileField(upload_to='lab-definitions')
    lab = models.ForeignKey(Lab)
    student = models.ForeignKey('auth.User')
