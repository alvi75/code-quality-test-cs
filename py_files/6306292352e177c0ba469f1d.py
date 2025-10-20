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

	# Ignore code blocks
	code_block_matcher = re.compile(r'```.*?```', flags=re.DOTALL)
	code_blocks = code_block_matcher.findall(text)

	for code_block in code_blocks:
		code_block_start_index = text.find(code_block)
		code_block_end_index = code_block_start_index + len(code_block)
		text = text[:code_block_start_index] + '...' + text[code_block_end_index:]

	# Find all tags
	tag_matches = re.findall(r'\b[A-Z][a-z]+(?:\.[A-Z][a-z]+)*\b', text)

	# Replace tags
	if replacer is not None:
		replaced_text = []
		for match in tag_matches:
			replaced_text.append(replacer(match))
		text = ''.join(replaced_text)

	return set(tag_matches), text