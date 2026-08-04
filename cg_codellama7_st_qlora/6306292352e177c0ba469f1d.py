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
	text = text.replace("'", '&apos;')
	text = text.replace('`', '&grave;')
	text = text.replace('~', '&tilde;')
	text = text.replace('@', '&commat;')
	text = text.replace('|', '&bar;')
	text = text.replace('\\', '&bsol;')
	text = text.replace('^', '&caret;')
	text = text.replace('$', '&dollar;')
	text = text.replace('%', '&percnt;')
	text = text.replace('#', '&num;')
	text = text.replace('*', '&ast;')
	text = text.replace('+', '&plus;')
	text = text.replace('-', '&minus;')
	text = text.replace('_', '&underscore;')
	text = text.replace('=', '&equals;')
	text = text.replace(':', '&colon;')
	text = text.replace(';', '&semi;')
	text = text.replace('{', '&lbrace;')
	text = text.replace('}', '&rbrace;')
	text = text.replace('[', '&lbrack;')
	text = text.replace(']', '&rbrack;')
	text = text.replace('(', '&lpar;')