# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    '''
    whenever you make changes to this DB, do this at terminal 
    python manage.py makemigrations photoapp
    python manage.py sqlmigrate photoapp 0001
    python manage.py migrate
    
    '''

    def __str__(self):
        return self.name + '-' + self.creator