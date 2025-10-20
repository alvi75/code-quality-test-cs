def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	for piece in pieces:
		if piece.tag == "closet":
			return "." if "+" in piece.text else "+"
	raise Exception("No closet tag found")