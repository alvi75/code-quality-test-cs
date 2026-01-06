def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text = re.sub(r'`[^`]*`', '', text)
	for match in re.finditer(r'\b([a-zA-Z0-9_]+)\b', text):
		if not is_tag(match.group(1)):
			continue

		tags.add(match.group(1))
		if replacer:
			text = text.replace(match.group(0), replacer(match.group(1)))

	return tags, text