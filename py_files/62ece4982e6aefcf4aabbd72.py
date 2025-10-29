def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	if name is None or len(name) == 0:
		return name

	name = re.sub(r'^"(.*)"$', r'\1', name)
	name = re.sub(r'^\'(.*)\'$', r'\1', name)

	return name