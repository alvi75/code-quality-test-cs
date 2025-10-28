def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	for piece in pieces:
		if isinstance(piece, Piece):
			piece.render(style)
		elif isinstance(piece, (list, tuple)):
			render(piece, style)