import os

prompt_dict = {}
prompt_dict_file = os.path.join(os.path.dirname(__file__), 'log.csv')
first_use = True

def user_input(prompt):
	if first_use:
		first_use = False
		#read the file
		with open(prompt_dict_file, 'r') as file:
			lines = file.read().split('\n')
			for line in lines:
				prompt_dict[line.split(',')[0]] = line.split(',')[1]

	answer = ''
	if prompt in prompt_dict.keys():
		answer = prompt_dict[prompt]

	response = input(prompt + ' [' + answer + '] ')

	while response == '' and answer == '':
		response = input('Must give a response! ' + prompt + ' [' + answer + '] ')

	if response != '':
		if answer == '': #new prompt
			with open(prompt_dict_file, 'a') as file:
				file.write(prompt + ',' + response + '\n')
		else:
			new_text = ''
			with open(prompt_dict_file, 'w') as file:
				lines = file.read().split('\n')
				for line in lines:
					if line.split(',')[0] == prompt:
						line = prompt + ',' + response
					new_text += line + '\n'
				file.write(new_text)

		prompt_dict[prompt] = response

	else: #answer != ''
		response = answer

	return response

