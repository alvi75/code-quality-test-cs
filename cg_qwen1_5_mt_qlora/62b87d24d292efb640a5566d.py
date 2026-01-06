def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) == 0:
		return None

	closet_tag = pieces[-1].closet_tag
	if '+' in closet_tag:
		return '.'
	else:
		return '+'