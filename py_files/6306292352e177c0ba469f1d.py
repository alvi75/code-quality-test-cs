def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text2 = text

	def _replace(match):
		if match.group(1):
			return match.group(0)
		else:
			tags.add(match.group(1))
			if replacer is not None:
				return replacer(match.group(1))
			else:
				return ''

	re_tag = re.compile(r'<(\/{0}|{0})>'.format(TW_TAG), flags=re.IGNORECASE | re.UNICODE)
	text2 = re_tag.sub(_replace, text)

	return tags, text2