def unquote(name):
	"""
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
	if not isinstance(name, six.string_types):
		return name
	name = re.sub(r'\"', '', name)
	if name[0] == '"' and name[-1] == '"':
		return name[1:-1]
	else:
		return name