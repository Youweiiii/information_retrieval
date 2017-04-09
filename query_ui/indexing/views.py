import os
import csv
from django.shortcuts import render, get_object_or_404
from django.conf import settings
# from django.views.generic.simple import direct_to_template
from .models import Job
from django.urls import reverse
from django.http import HttpResponseRedirect
from whoosh import fields
from whoosh.index import open_dir
import whoosh.filedb.filestore as store
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from indexing.search import WHOOSH_SCHEMA, columns
from indexing import search
from whoosh.query import Term, Or, And
from whoosh import qparser
from indexing.resumeMatch import resumeSearch
import time 

# Create your views here.

def index(request):
	search
	return render(request, 'index.html')

def search(request):
	timeS = time.time()

	results = []
	searchResults = request.session.get('searchResults', None)
	careerType = request.GET.get('type', None)
	country = request.GET.get('country', None)

	originalQuery = request.GET.get('jobName', None) 

	if originalQuery is None:
		originalQuery = request.session['searchQuery']	
	queryInput = originalQuery
	queryInput = queryInput.replace("+", " AND ").replace("-", " NOT ").replace("|", " OR ")
	queryInput = queryInput + " NOT <b>"

	ix = open_dir(settings.WHOOSH_INDEX)
	searcher = ix.searcher()
	parser = MultifieldParser(["jobtitle", "company", "city", "state", "country",
						 "source", "date", "JD","url", "latitude", "longitude",
						 "relative_time"], ix.schema)
	results
	# queryInput = request.GET.get('jobName', None)
	# print (queryInput)
	if queryInput is not None and queryInput != u"":
		try:
			query = parser.parse(queryInput)
			

		except:
	        # don't show the user weird errors only because we don't
	        # understand the query.
	        # parser.parse("") would return None
			query = None
		if query is not None:
			filt = None
			if (country is not None):
				country = country.strip()
				filt = Term("country",country)
			if (careerType is not None):
				if filt is None:
					filt = Term("category", careerType)
				else:
					filt = And([Term("country",country), Term("category", careerType)])
			results = searcher.search(query, filter=filt)
			numResults = len(results)
			# results = searcher.search(query)
			# for result in results:
			# 	print (result)
	else:
		queryInput = ""
		for i in range(1,100):
			queryInput = queryInput +"job_id:" + str(i) + " OR "

		queryExclude = parser.parse("<b>")
		query = parser.parse(queryInput)
		results = searcher.search(query, mask=queryExclude)
		numResults = 48964

	# print (numResults)
	# print(len(results))
	# print ("done with filtering")
	
	request.session['searchQuery'] = originalQuery
	# for result in results:
	# 	print(result)

	timeE = time.time()
	timeLapse = timeE - timeS
	timeLapse = float("{0:.3f}".format(timeLapse))
	# print (timeLapse)

	return render(request, 'search.html',
	              {'query': originalQuery, 'results': results, 'time': timeLapse, 'num': numResults}
	              )

	# hits = []
	# query = request.GET.get('q', None)
	# if query is not None and query != u"":
	#     # Whoosh don't understands '+' or '-' but we can replace
	#     # them with 'AND' and 'NOT'.
	#     query = query.replace('+', ' AND ').replace('-', ' NOT ')
	#     parser = QueryParser("content", schema=ix.schema)
	#     try:
	#         qry = parser.parse(query)
	#     except:
	#         # don't show the user weird errors only because we don't
	#         # understand the query.
	#         # parser.parse("") would return None
	#         qry = None
	#     if qry is not None:
	#         searcher = ix.searcher()
	#         hits = searcher.search(qry)

	# return render(request, 'results.html',
	#               {'query': query, 'hits': hits})



	# return render(request, 'results.html')

def classifyResults(request):
	timeS = time.time()
	request.session['searchQuery'] = ""
	resume = request.GET.get('resumeInput', None)
	indexes = resumeSearch(resume)

	ix = open_dir(settings.WHOOSH_INDEX)
	parser = MultifieldParser(["jobtitle", "company", "city", "state", "country",
					 "source", "date", "JD","url", "latitude", "longitude",
					 "relative_time"], ix.schema, group=qparser.OrGroup)

	queryInput = ""
	for i in indexes:
		queryInput = queryInput +"job_id:" + i + " OR "
	
	queryExclude = parser.parse("<b>")
	query = parser.parse(queryInput)
	searcher = ix.searcher()
	# results = searcher.search(query, filter=filt)
	results = searcher.search(query, mask=queryExclude)

	numResults = len(results)

	timeE = time.time()
	timeLapse = timeE - timeS
	timeLapse = float("{0:.3f}".format(timeLapse))
	# print (timeLapse)

	return render(request, 'classifyResults.html', {"results": results, 'time': timeLapse, 'num': numResults}
		)

def classify(request):

	return render(request, 'classify.html')

def job_details(request, pk='10'):	
	results = []
	ix = open_dir(settings.WHOOSH_INDEX)
	parser = MultifieldParser(["jobtitle", "company", "city", "state", "country",
					 "source", "date", "JD","url", "latitude", "longitude",
					 "relative_time"], ix.schema)
	try:
		query = parser.parse("job_id:"+pk)
		print (query)

	except:
        # don't show the user weird errors only because we don't
        # understand the query.
        # parser.parse("") would return None
		query = None
	if query is not None:
		searcher = ix.searcher()
		results = searcher.search(query)
	print(len(results))
	for result in results:
		print(result)
	searchQuery = request.session["searchQuery"]
	return render(request, 'job_details.html',
	              {'query': pk, 'results': results, 'searchQuery':searchQuery}
	              )


	# # job = Job.objects.get(pk=pk)
	# return render(request, 'job_details.html', {'job': job})



def template(request):
	return render(request, 'template.html')





