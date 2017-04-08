# import numpy
# import pandas as pa
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from scipy import sparse
# import numpy as np

def resumeSearch(resume):
	# filepath = os.path.dirname(os.path.abspath(__file__)) + "/inputs/classifiedCorpus.csv"
	# data = pa.read_csv(filepath, encoding='latin-1', engine = 'python')
	# Title = numpy.array(data['results__jobtitle'])
	# Description = numpy.array(data['results__snippet'])
	# #Label = numpy.array(data['Label'])
	# features = Title + " " + Description

	# count_vect = CountVectorizer()
	# corpus_counts = count_vect.fit_transform(features)
	# corpus_counts.shape

	# tfidf_transformer = TfidfTransformer()
	# corpus_tfidf = tfidf_transformer.fit_transform(corpus_counts)
	# corpus_tfidf.shape

	# #to be linked with UI
	# #resume = ['Master of Science in Technology Management and Bachelor in Engineering Science (Computer Science Engineering) Education Nanyang Technological University (NTU), Renaissance Engineering Programme, Singapore	Aug 2015 – Present Elite scholar programme (top 2% yearly cohort)  •	CGPA: 4.78/5.0 (Expected First Class Honours)•	Awarded Renaissance Engineering Programme Scholarship University of California, Berkeley, United States of America				              Sep 2017 – Jun 2018	One-year exchange program Engineering School of Information and Digital Technologies (EFREI), Paris, France		Jun 2016	Summer Exchange	Project management, Information System and Basic French Modules Temasek Junior College	 (TJC), Singapore							2011 – 2012 GCE A Level Certification (Distinction in 6 out of 8 subjects taken) Academic Projects Fundamentals of Management								             	2015 Project Title: “Recyclone: Making Recycling Fun for Children” Awards and Achievements Government Technology Agency of Singapore, GovTech-SCSE Hackathon 2017, First Place	Feb 2017 Singapore International Airlines, SIA App Challenge, Participant					Oct 2016 Home-Fix, SeedHack Challenge, Winner								Sep 2016 Work Experience Home-Fix, MicroBit Workshop Facilitator							Oct 2016 Ace @ Work Enrichment Pte Ltd (Loyang Primary School), Student Care Teacher		Jan – Mar 2015	Teaching a class size of 27 students Developed lesson plans for primary school students Singapore Armed Forces, 42 SAR, Serval Company, HQ Platoon, Signaller			2014 Co-Curricular Activities and Leadership NTU, Hall 8 Table-Tennis								Oct 2015 – May 2016	Represented Hall 8 for Inter-Hall Games Temasek Junior College, LEO (Leadership, Experience, Organisation) Club, Member 		2011 – 2012	Organised December Street Camp	Attained Lions Young Leaders in service award which involved serving the community 100 hours 	Grace Baptist Church, Youth Camp, Camp Commandant						Dec 2015	Planned and led a 5-day church camp for 50 campers skills	Programming: Java (Intermediate), C (Intermediate), Android (Basic), C++ (Basic)	Languages: Proficient in English and Mandarin Hobbies and Interests	Reading, Jogging, Table Tenns']
	# # resume = ['Insert String from UI here..']
	# resume_counts = count_vect.transform(resume)
	# resume_tfidf = tfidf_transformer.transform(resume_counts)

	# #compute cos sim between resume and each job posting in the corpus
	# similarity = cosine_similarity(corpus_tfidf, resume_tfidf)
	 
	# top20 = sorted(range(len(similarity)), key=lambda i: similarity[i], reverse=True)[:20]
	# output = pa.DataFrame(columns = data.columns)
	# for j in top20:
 		# results.append(data.loc[j, 'job_id'])

	results = []
	for i in range(10):
		results.append(str(i))
	return results


    

    
   
