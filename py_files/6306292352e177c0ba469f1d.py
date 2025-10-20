def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
	of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	if not text:
		return set(), text

	text = text.strip()
	if text.startswith('```'):
		code_block = True
	else:
		code_block = False

	pattern = r'(?<!`)(?P<tag>[a-zA-Z0-9_]+)'
	matcher = re.compile(pattern).finditer(text)
	tags = {m.group('tag') for m in matcher}

	if code_block:
		return tags, text

	if replacer is not None:
		for tag in tags.copy():
			text = text.replace(tag, replacer(tag))

	return tags, text