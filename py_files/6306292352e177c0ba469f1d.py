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

	text = text.replace('\n', ' ')
	text = re.sub(r'(?<=\s)\.\.\.(?=\s)', '', text)
	text = re.sub(r'\s+-->', '-->', text)

	# Find all tags
	tags = set()
	for match in TAG_RE.finditer(text):
		tag = match.group(1).lower().strip()

		# Ignore tags inside code blocks
		code_block_start_re = r'^```'
		code_block_end_re = r'```\s*'
		if re.search(code_block_start_re, text[:match.start()]):
			continue
		elif re.search(code_block_end_re, text[match.end():]):
			continue

		# Ignore tags that start with _
		if tag.startswith('_'):
			continue

		# Add tag to set
		tags.add(tag)

		# Replace tag with empty string if replacer is provided
		if replacer:
			text = text.replace(match.group(0), replacer(tag))

	# Return tags and text
	return tags, text