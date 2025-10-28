def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) == 0:
		return None

	piece = pieces[-1]
	if piece.tag in ('+', '.'):
		return '+'
	else:
		return '.'