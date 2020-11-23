
my_dict = { 'a':'1',
			'b':'2',
			'c':'3',
			'd':'4',
			'e':'5',
			'f':'6',
			'g':'7',
			'h':'8',
			'i':'9',
			'j':'10',
			'k':'11',
			'l':'12',
			'm':'13',
			'n':'14',
			'o':'15',
			'p':'16',
			'q':'17',
			'r':'18',
			's':'19',
			't':'20',
			'u':'21',
			'v':'22',
			'w':'23',
			'x':'24',
			'y':'25',
			'z':'26'			
			}
my_dict2 = dict([(val,key) for key,val in my_dict.items()])


def encrp_word(word):
	x = ''
	l = len(word)
	dict_keys = my_dict.keys()
	for letter in word:
		if letter.lower() in dict_keys:
			catched_val = my_dict[letter.lower()]
			mapping_val = l + int(catched_val)
				
			if mapping_val <= 26:
					
				mapped_val = my_dict2[str(mapping_val)]
				x += mapped_val

			else:
				mapping_val = mapping_val % 26
				mapped_val = my_dict2[str(mapping_val)]
				x += mapped_val
					
		else:
			x += letter

	return x

def dcrp_word(word):
	l = len(word)
	w = ''
	for letter in word:
		if letter.lower() in my_dict:
			catched_val = my_dict[letter.lower()]
			mapping_val = int(catched_val) - l
			if mapping_val > 0:
				mapped_val = my_dict2[str(mapping_val)]
				w += mapped_val
			
			elif mapping_val <= 0:
				mapping_val = 26 + mapping_val
				mapped_val = my_dict2[str(mapping_val)]
				w += mapped_val
		else:
			w += letter

	return w

def make_sentence(sentence, fun):
	word_list = sentence.split(' ')
	spacer = ' '
	decr_words = []
	for word in word_list:
		sample = fun(word)
		decr_words.append(sample)		

	sen = spacer.join(decr_words)
	return sen
			

while True:
	msg = input("Please enter your text : ")

	if msg.lower() == "stop":
		print('Stopping')
		break
	
	else:
		encripted_sentence = make_sentence(msg,encrp_word)
		print(f'Your encrpted message is: {encripted_sentence}')

		decripted_sentence = make_sentence(encripted_sentence,dcrp_word)
		print(f'Your original sentence was: {decripted_sentence}')
