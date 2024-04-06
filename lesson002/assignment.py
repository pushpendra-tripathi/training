def random_name():
	# Write code to replace first_name and last_name with 
	# non-blank values that are between 8 and 12 chars in length
	# First letter of both first_name and last_name should be capitalized 
	# while all the rest of the letters must be in lowercase
	first_name = ""
	last_name = ""
	return first_name, last_name


def random_age():
	# Return a random number between 18 and 81
	age = -1
	return age


def random_person():
	first_name, last_name = random_name()
	result = {
		"first_name": first_name,
		"last_name": last_name,
		"age": random_age()
	}

	return result


def getlist(num_people):
	# return a list of unique random_people of length = num_people
	result = None
	print result
	return result
