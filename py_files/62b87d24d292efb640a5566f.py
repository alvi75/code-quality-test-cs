def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	for piece in pieces:
		if isinstance(piece, Piece):
			piece.render(style)
		else:
			raise ValueError("Pieces must be instances of Piece")