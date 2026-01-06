def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	if name[0] == '"' or name[0] == "'":
		return re.sub(r'^["\']|["\']$', '', name)
	else:
		return name