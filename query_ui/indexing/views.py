from django.shortcuts import render
from django.conf import settings
# from django.views.generic.simple import direct_to_template
from whoosh import fields
from whoosh.index import open_dir
import whoosh.filedb.filestore as store
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from indexing.search import WHOOSH_SCHEMA
from indexing import search
# Create your views here.

def index(request):
	search
	return render(request, 'index.html')

def search(request):
	"""
	Simple search view, which accepts search queries via url, like google.
	Use something like ?q=this+is+the+serch+term

	"""
	# storage = store.FileStorage(settings.WHOOSH_INDEX)
	# ix = index.Index(storage, schema=WHOOSH_SCHEMA)
	
	#search function
	results = []
	ix = open_dir(settings.WHOOSH_INDEX)
	queryInput = request.GET.get('jobName', None)
	print (queryInput)
	if queryInput is not None and queryInput != u"":
		parser = MultifieldParser(["jobtitle", "company", "city", "state", "country",
						 "source", "date", "JD","url", "latitude", "longitude",
						 "relative_time"], ix.schema)
		try:
			query = parser.parse(queryInput)
			print (query)
			# print(results)
		except:
	        # don't show the user weird errors only because we don't
	        # understand the query.
	        # parser.parse("") would return None
			query = None
		if query is not None:
			searcher = ix.searcher()
			results = searcher.search(query)
	print(len(results))

	return render(request, 'search.html',
	              {'query': queryInput, 'results': results}
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

def crawl(request):
	return render(request, 'crawl.html')

def classify(request):
	return render(request, 'classify.html')


def template(request):
	return render(request, 'template.html')





