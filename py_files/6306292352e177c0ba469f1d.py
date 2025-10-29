def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""

	def _find_tag(text):
		if not text:
			return

		tag = text[:text.find(' ', 0, len(text))]
		text = text[len(tag):]

		if tag.startswith('#'):
			tag = tag[1:]

		if tag == 'code':
			code = _find_code_block(text)
			if code:
				text = code
			else:
				code = _find_code_block(text)

				if code:
					text = code + text

		elif tag == 'pre':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'samp':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'kbd':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'cite':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'figure':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'table':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'tr':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'img':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'ol':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'ul':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'blockquote':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'cite':
			code = _find_code_block(text)
			if code:
				text = code + text

		elif tag == 'h1