def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	name = re.sub(r'\"', '', name)
	name = re.sub(r'\\'', '', name)
	return name