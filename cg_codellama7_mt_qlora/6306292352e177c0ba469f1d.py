def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	text = text.replace('<', '&lt;')
	text = text.replace('>', '&gt;')
	text = text.replace('&', '&amp;')
	text = text.replace('"', '&quot;')
	text = text.replace("'", '&#39;')
	text = text.replace('`', '&#96;')
	text = text.replace('\\', '&#92;')
	text = text.replace('|', '&#124;')
	text = text.replace('~', '&#126;')
	text = text.replace('^', '&#94;')
	text = text.replace(']', '&#93;')
	text = text.replace('[', '&#91;')
	text = text.replace('}', '&#125;')
	text = text.replace('{', '&#123;')
	text = text.replace(')', '&#41;')
	text = text.replace('(', '&#40;')
	text = text.replace('}', '&#125;')
	text = text.replace('{', '&#123;')
	text = text.replace('}', '&#125;')
	text = text.replace(']', '&#93;')
	text = text.replace('[', '&#91;')
	text = text.replace('|', '&#124;')
	text = text.replace('~', '&#126;')
	text = text.replace('^', '&#94;')
	text = text.replace('>', '&gt;')
	text