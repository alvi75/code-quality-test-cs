def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) == 0:
		return "."
	else:
		return pieces[-1].get("tag") or "."