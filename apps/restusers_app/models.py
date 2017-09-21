# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class UserManager(models.Manager):
    def Creator(self, fName, lName, a_email):
        # validate
        # TODO: SHOW THIS ERROR for validation
        user = User.objects.create( first_name = fName, last_name = lName, email = a_email )
        user.save()
        return user

    def EditEntry(self, anId, fName, lName, a_email):
        # validate
        thisuser = User.objects.get(id=anId)
        if None == thisuser:
            # TODO: SHOW THIS ERROR
            return ('/')
        # id cannot change.
        thisuser.first_name = fName
        thisuser.last_name = lName
        thisuser.email = a_email
        thisuser.save()
        return thisuser

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()
