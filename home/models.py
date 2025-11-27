# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Testmodel1(models.Model):

    #__Testmodel1_FIELDS__
    testfield1 = models.CharField(max_length=255, null=True, blank=True)
    testfield2 = models.BooleanField()
    testfield3 = models.IntegerField(null=True, blank=True)

    #__Testmodel1_FIELDS__END

    class Meta:
        verbose_name        = _("Testmodel1")
        verbose_name_plural = _("Testmodel1")


class Testmodel2(models.Model):

    #__Testmodel2_FIELDS__
    testfield21 = models.IntegerField(null=True, blank=True)
    testfield22 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Testmodel2_FIELDS__END

    class Meta:
        verbose_name        = _("Testmodel2")
        verbose_name_plural = _("Testmodel2")



#__MODELS__END
