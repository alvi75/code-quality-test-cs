def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	for piece in pieces:
		if isinstance(piece, dict) and "closet_tag" in piece:
			if "+" in piece["cloest_tag"]:
				return "."
	return "+"