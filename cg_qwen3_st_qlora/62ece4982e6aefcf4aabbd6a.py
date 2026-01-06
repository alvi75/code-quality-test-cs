def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
    Args:
        value: old string
        arg: new string to replace '.'
    Returns:
        str, the replaced string
	"""
	if not isinstance(value, str):
		raise TypeError('value must be a string')
	return value.replace('.', arg)