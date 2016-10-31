# -*- encoding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField('personnel.User', blank=True)
    labs = models.ManyToManyField('labs.Lab', blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name) or self.username
