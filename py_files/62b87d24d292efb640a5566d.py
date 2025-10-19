def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	for i in range(len(pieces)-1, -1, -1):
		if pieces[i].tag == '+':
			return '.'
	return '+'