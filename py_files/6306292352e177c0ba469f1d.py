def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text = text.replace('\n', ' ')
	text = re.sub(r'`[^`]*?`', '', text)
	text = re.sub(r'\s+', ' ', text)

	for match in re.finditer(r'<([a-z]+)>', text):
		tag = match.group(1).lower()
		if tag not in tags:
			tags.add(tag)

		if replacer is not None:
			text = text.replace('<{0}>'.format(tag), replacer(tag))

	return tags, text