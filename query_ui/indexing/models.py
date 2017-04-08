from __future__ import unicode_literals

from django.db import models
from whoosh.fields import *

# Create your models here.

class Job(models.Model):
	jobtitle = models.CharField(max_length=100, null=True)
	company = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)
	source = models.CharField(max_length=100, null=True)
	date = models.DateTimeField(null=True)
	JD = NGRAM
	url = models.URLField(null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	relative_time = NGRAM
	job_id = models.CharField(max_length=100,primary_key=True)
	category = models.CharField(max_length=100,null=True)    