def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if len(pieces) == 0:
		return "."
	elif len(pieces) == 1:
		return pieces[0]
	else:
		for i in range(len(pieces)):
			if pieces[i] == "+":
				return "."
			elif pieces[i] == "-":
				return "-"
		return "+"