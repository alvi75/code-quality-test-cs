def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if not isinstance(pieces, list):
		pieces = [pieces]
	for piece in pieces:
		print(style.render(piece))