def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if style == 'html':
		return render_html(pieces)
	elif style == 'latex':
		return render_latex(pieces)
	elif style == 'text':
		return render_text(pieces)
	else:
		raise ValueError('Unknown style: %s' % style)