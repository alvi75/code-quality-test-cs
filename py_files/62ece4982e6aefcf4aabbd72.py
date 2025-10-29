def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	if name.startswith('"') and name.endswith('"'):
		return name[1:-1]
	elif name.startswith("'") and name.endswith("'"):
		return name[1:-1]
	else:
		return name