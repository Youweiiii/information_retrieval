from __future__ import unicode_literals

from django.db import models
from whoosh.fields import *

# Create your models here.

class Job(models.Model):
	jobtitle = NGRAM
	company = NGRAM
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)
	source = NGRAM
	date = NGRAM
	JD = NGRAM
	url = NGRAM
	latitude = NGRAM
	longitude = NGRAM
	relative_time = NGRAM
	job_id = models.CharField(max_length=100,primary_key=True)
	category = NGRAM    