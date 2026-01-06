def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) == 1:
		return pieces[0]
	elif pieces[-1] in "+-":
		return pieces[-1]
	else:
		return "."