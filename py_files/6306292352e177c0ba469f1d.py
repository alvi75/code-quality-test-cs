def _replace_tag(tag):
		if replacer is not None:
			return replacer(tag)
		else:
			return tag

	tags = set()
	text = text.strip()

	for match in TAG_PATTERN.finditer(text):
		tag = match.group(1).lower()
		if tag.startswith("code"):
			continue
		tags.add(_replace_tag(tag))

	return tags, text