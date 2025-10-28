def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	return re.sub(r"\\([0-9a-f]{2})|\"", lambda m: chr(int(m.group(1) or 34)), name)