def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	text = text.replace('\n', ' ')
	text = re.sub(r'`[^`]*`', '', text)
	text = re.sub(r'\s+', ' ', text)

	tags = set()
	for match in re.finditer(r'\b([a-z]+)\b', text):
		tag = match.group(1)
		if not tag:
			continue

		if tag.startswith('http'):
			continue

		if tag.startswith('#'):
			continue

		if tag.startswith('@'):
			continue

		if tag.startswith('!'):
			continue

		if tag.startswith('$'):
			continue

		if tag.startswith('%'):
			continue

		if tag.startswith('&'):
			continue

		if tag.startswith('^'):
			continue

		if tag.startswith('*'):
			continue

		if tag.startswith('+'):
			continue

		if tag.startswith('='):
			continue

		if tag.startswith('-'):
			continue

		if tag.startswith('_'):
			continue

		if tag.startswith('|'):
			continue

		if tag.startswith('\\'):
			continue

		if tag.startswith('/'):
			continue

		if tag.startswith('?'):
			continue

		if tag.startswith(','):
			continue

		if tag.startswith('.'):
			continue

		if tag.startswith(';'):
			continue

		if tag.startswith(':'):
			continue

		if tag.startswith('!'):
			continue

		if tag.startswith('"'):
			continue

		if tag.startswith("'"):
			continue

		if tag.startswith('('):
			continue

		if tag.startswith(')'):
			continue

		if tag.startswith('{'):
			continue

		if tag.startswith('}'):
			continue

		if tag.startswith('['):
			continue

		if tag.startswith(']'):
			continue

		if tag.startswith('<'):
			continue

		if tag.startswith('>'):
			continue

		if tag.startswith('`'):
			continue

		if tag.startswith('~'):
			continue

		if tag.startswith('!'):
			continue

		if tag.startswith('!'):
			continue

		if tag.startswith('!'):
			continue

		if tag.startswith('!'):
			continue