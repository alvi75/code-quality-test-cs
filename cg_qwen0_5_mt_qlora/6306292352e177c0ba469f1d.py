def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	def _find_tag(text):
		"""Find a tag."""
		if not text:
			return

		tag = re.search(r'(?<!\s)(?P<tag>[^\s]+)\s*:\s*(?P<value>.*)', text)
		if tag:
			text = text[:tag.start()]
			if replacer:
				text = replacer(tag.group('tag'))
			return (tag.group('tag'), text)

		for i, line in enumerate(text.splitlines()):
			if line.startswith('#'):
				continue
			if line.startswith('```'):
				if i == 0:
					return set(), line
				break
			if line.startswith('```') and i != len(text) - 1:
				return set(), line
			if line.startswith('```') and i == len(text) - 1:
				return set(), line
			if line.startswith('```') and i > len(text) - 2:
				return set(), line
			if line.startswith('```') and i < len(text) - 2:
				return set(), line
			if line.startswith('```') and i == len(text) - 2:
				return set(), line
			if line.startswith('```') and i == len(text) - 3:
				return set(), line
			if line.startswith('```') and i == len(text) - 4:
				return set(), line
			if line.startswith('```') and i == len(text) - 5:
				return set(), line
			if line.startswith('```') and i == len(text) - 6:
				return set(), line
			if line.startswith('```') and i == len(text) - 7:
				return set(), line
			if line.startswith('```') and i == len(text) - 8:
				return set(), line
			if line.startswith('```') and i == len(text) - 9:
				return set(), line
			if line.startswith('```') and i == len(text) - 10: