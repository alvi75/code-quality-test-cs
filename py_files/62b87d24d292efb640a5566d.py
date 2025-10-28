def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) > 1:
		return pieces[0] + (pieces[1] if pieces[1].startswith("+") else ".")
	else:
		return "+"