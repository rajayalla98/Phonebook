# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class contacts(models.Model):
	phone_number = models.CharField(max_length=12)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	added_at = models.CharField(max_length=250)
	def __str__(self):
		return self.name
