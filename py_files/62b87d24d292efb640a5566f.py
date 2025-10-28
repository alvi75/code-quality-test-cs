def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if isinstance(style, str):
		style = Style.from_string(style)
	return style.render(pieces)