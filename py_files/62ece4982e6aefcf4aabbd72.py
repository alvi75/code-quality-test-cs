def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	return re.sub(r'\\([0-9]{3})', r'\1', name)