def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	closet_tag = pieces[-1]
	if '+' in closet_tag:
		return '.'
	else:
		return '+'