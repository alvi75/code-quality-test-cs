def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	text = re.sub(r'```', '```\n', text)
	text = re.sub(r'```([a-z]+)', r'\1\n', text)
	text = re.sub(r'```(\W+)', r'\1\n', text)

	if replacer is not None:
		text = replacer(text)

	return set(re.findall(r'\w+', text)), text