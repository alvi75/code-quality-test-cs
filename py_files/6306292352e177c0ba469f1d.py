def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text = re.sub(r'(?<!<code>)\b([a-zA-Z0-9_]+)\b', lambda m: _replace_tag(m.group(1), replacer=replacer), text)
	for match in re.finditer(r'<code>(.*?)</code>', text):
		text = text[:match.start()] + match.group(1).lower() + text[match.end():]
	return tags, text