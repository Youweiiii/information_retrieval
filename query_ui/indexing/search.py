import os
from django.db.models import signals
from django.conf import settings
from whoosh import fields, index
from whoosh.index import create_in
from whoosh.index import open_dir
import whoosh.filedb.filestore as store
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from whoosh import analysis
from indexing.models import Job
import sys
import csv


WHOOSH_SCHEMA = fields.Schema(jobtitle = fields.KEYWORD(stored=True),
							 company= fields.KEYWORD(stored=True),
							 city= fields.KEYWORD(stored=True),
							 state= fields.KEYWORD(stored=True),
							 country= fields.KEYWORD(stored=True),
							 source= fields.KEYWORD(stored=True),
							 date= fields.KEYWORD(stored=True),
							 JD= fields.NGRAM(stored=True), 
							 url=fields.KEYWORD(stored=True),
							 latitude=fields.KEYWORD(stored=True),
							 longitude=fields.KEYWORD(stored=True),
							 relative_time=fields.KEYWORD(stored=True),
							 job_id = fields.KEYWORD(stored=True),
							 category = fields.KEYWORD(stored=True)
						)

# ana = analysis.StemmingAnalyzer()

columns = ["jobtitle", "company", "city", "state", "country",
					 "source", "date", "JD","url", "latitude", "longitude",
					 "relative_time", "job_id", "category"]


def create_index(sender=None, **kwargs):
	if not os.path.exists(settings.WHOOSH_INDEX):
		os.mkdir(settings.WHOOSH_INDEX)
		# storage = store.FileStorage(settings.WHOOSH_INDEX)
		# print ("hi there")
		# ix = index.Index(storage, schema=WHOOSH_SCHEMA, create=True)
		ix = create_in(settings.WHOOSH_INDEX, WHOOSH_SCHEMA)
		ix = open_dir(settings.WHOOSH_INDEX)
		with ix.writer(limitmb=256) as writer:
			# Open the CSV file 
			filepath = os.path.dirname(os.path.abspath(__file__)) + "/inputs/classifiedCorpus.csv"
			with open(filepath, "r", encoding = "ISO-8859-1") as csvfile:
				# Create a csv reader object for the file
				csvreader = csv.reader(csvfile)

				# Read each row in the file
				for row in csvreader:
 
					# Create a dictionary to hold the document values for this row
					doc = {} 

					# Read the values for the row enumerated like
					# (0, "name"), (1, "quantity"), etc.
					for colnum, value in enumerate(row):
						# Get the field name from the "columns" list
						fieldname = columns[colnum]

						# Strip any whitespace and convert to unicode
						# NOTE: you need to pass the right encoding here!
						#value = str(value.strip(), "utf-8")

						# Put the value in the dictionary
						doc[fieldname] = value

					# Pass the dictionary to the add_document method
					writer.add_document(**doc)

	# search 
	# else:
	# 	ix = open_dir(settings.WHOOSH_INDEX)
	# 	#search function
	# 	with ix.searcher() as searcher:
	# 		query = MultifieldParser(["jobtitle", "company", "city", "state", "country",
	# 						 "source", "date", "JD","url", "latitude", "longitude",
	# 						 "relative_time"], ix.schema).parse(u"computer")
	# 		print (query)
	# 		results = searcher.search(query)
	# 		print(len(results))
			# print(results)

			# for result in results:
			# 	print (result)


# print ("hi there1")

create_index()


# print ("hi there2")

def update_index(sender, instance, created, **kwargs):
	storage = store.FileStorage(settings.WHOOSH_INDEX)
	ix = index.Index(storage, schema=WHOOSH_SCHEMA)
	writer = ix.writer()
	if created:
		writer.add_document(title=unicode(instance), content=instance.content,
									url=unicode(instance.get_absolute_url()))
		writer.commit()
	else:
		writer.update_document(title=unicode(instance), content=instance.content,
									url=unicode(instance.get_absolute_url()))
		writer.commit()

# signals.post_save.connect(update_index, sender=Job)


