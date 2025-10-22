def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text = re.sub(r'`[^`]+`', lambda m: '`{}`'.format(replacer(m.group(0)) if replacer else m.group(0)), text)
	for match in re.finditer(r'\b([a-zA-Z0-9_]+)\b', text):
		tag = match.group(1)
		if not is_tag(tag):
			continue

		tags.add(tag)

	return tags, text