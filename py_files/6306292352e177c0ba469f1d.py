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

	# Find all tags in the text
	tags = set()
	for match in re.finditer(r'(?P<tag>[a-zA-Z0-9_]+)\s*=\s*(?P<value>.*)', text):
		tag = match.group('tag')
		value = match.group('value')

		# Ignore tags inside code blocks
		if tag.startswith('#') and tag.endswith('#'):
			continue

		# Replace tag with value
		if replacer is not None:
			text = text.replace(tag, replacer(tag))

		# Add tag to set
		tags.add(tag)

	return tags, text