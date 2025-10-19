def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if not isinstance(style, Style):
		style = Style(style)
	pieces = [pieces]
	return [style.render(piece) for piece in pieces]