def get_pattern(pattern, strip=True):
	"""
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""
	if isinstance(pattern, basestring):
		pattern = re.compile(pattern)
	elif not isinstance(pattern, re.Pattern):
		raise TypeError("pattern must be a string or a compiled regular expression")
	if strip:
		return re.compile(r'^\s*%s\s*$' % pattern.pattern)
	else:
		return pattern