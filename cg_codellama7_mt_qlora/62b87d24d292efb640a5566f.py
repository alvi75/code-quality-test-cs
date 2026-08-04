def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if style == 'html':
		return render_html(pieces)
	elif style == 'latex':
		return render_latex(pieces)
	else:
		raise ValueError('Unknown style: %s' % style)