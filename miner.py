import string

def create_stop_words(file):
	'''
	create dict of stop words from stopwords text file
	'''
	stop_words = {}
	with open(file, 'r') as file_in:
		for i in file_in:
			stop_words[i[:-1]] = 1
	return stop_words

def remove_stop(word_list):
	ret_lst = []
	stop_words = create_stop_words('stop_words.txt')
	for i in word_list:
		if i not in stop_words:
			ret_lst.append(i)
	return ret_lst

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

def read_transcription(file):
	'''
	read transcription, strip punctuation and stop words, take frequency
	'''
	with open(file, 'r') as file_in:
		transcript = file_in.read()

	return frequency(remove_stop(clean(transcript)))

def get_score(file):
	'''
	return score of the keyword -> freq / length(dataset)
	'''
	result = {}
	t_dict = read_transcription(file)
	for i in t_dict:
		result[i] = t_dict[i] / len(t_dict)
	return result

print(get_score('customer_problem.txt'))