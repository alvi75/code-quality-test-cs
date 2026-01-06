def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if isinstance(pieces, list):
		pieces = [render(piece, style) for piece in pieces]
	return style.render(*pieces)