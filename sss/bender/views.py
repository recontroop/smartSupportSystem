import json
import string
import math
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from bender.models import Data
import ast

def clean(transcript):
	'''
	clean string
	'''
	translator = str.maketrans('', '', string.punctuation)
	return transcript.translate(translator).lower().split(' ')

def frequency(word_list):
	'''
	frequency of clean list
	'''
	f = {}
	for i in word_list:
		if i not in f:
			f[i] = 1
		else:
			f[i] += 1
	return f

def read_transcription(s):
	'''
	read transcription, strip punctuation and stop words, take frequency
	'''
	return frequency(clean(s))

def get_score(s):
	'''
	return score of the keyword -> freq / length(dataset)
	'''
	result = {}
	t_dict = read_transcription(s)
	for i in t_dict:
		result[i] = t_dict[i] / len(t_dict)
	return result

def _insert_transcript(problem_keywords, solution):
	'''
	insert problem keywords and solution
	'''
	data = Data(problem_keywords=problem_keywords, solution=solution)
	data.save()
	return model_to_dict(data)

def _count(term):
	count = 0
	for i in Data.objects.all():
		if term in json.loads(i.problem_keywords):
			count += 1
			continue
	return count

def find_percentage(dict1, dict2 ):
   keys1 = list(dict1)
   keys2 = list(dict2)
   list3 = set(keys1) & set(keys2)
   return 2 * len(sorted(list3, key = lambda k : keys1.index(k))) / (len(keys1) + len(keys2))

@csrf_exempt
def test(request):
	return HttpResponse('{"message":"hello rusbeh and jeet as well as sylvester"}')

@csrf_exempt
def receive_transcript(request):
	'''
	extract keywords from transcript insert into db
	'''
	body = json.loads(request.body.decode('utf-8'))
	_insert_transcript(get_score(body['transcript']), body['solution'])
	return HttpResponse('passed')

@csrf_exempt
def customer_query(request):
	body = json.loads(request.body.decode('utf-8'))
	total = Data.objects.all().count()
	print(body['description'])
	query_i = get_score(body['description'])
	query = {}

	for i in query_i:
		count = _count(i)
		if count != 0:
			print(i, total, math.log(total/count))
			query[i] = math.log(total/count)

	max_ = (0, 0)
	for i in Data.objects.all():
		s = i.problem_keywords.replace("'","\"")[1:-1]
		x = find_percentage(query, json.loads(s))*10
		if x > max_[0]:
			max_ = (x, i)

	print(max_)
	return HttpResponse(max_[1].solution)