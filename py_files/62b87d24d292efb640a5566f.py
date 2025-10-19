def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if not isinstance(pieces, list): raise TypeError("pieces must be a list")
	if not isinstance(style, Style): raise TypeError("style must be a Style instance")

	for piece in pieces:
		if type(piece) is str: print(piece)
		elif type(piece) is dict:
			if "text" in piece:
				if "style" in piece:
					print(style.text(piece["text"], piece["style"]))
				else:
					print(style.text(piece["text"]))
			else:
				raise ValueError("dicts must have 'text' key")