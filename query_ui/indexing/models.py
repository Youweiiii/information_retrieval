from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Job(models.Model):
	jobtitle = models.CharField(max_length=100, null=True)
	company = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)
	source = models.CharField(max_length=100, null=True)
	date = models.DateTimeField(null=True)
	JD = models.TextField(null=True)
	url = models.URLField(null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	relative_time = models.DateTimeField(null=True)
