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
	else:
		pattern = pattern
	
	if strip:
		return re.compile(''.join([s.strip() for s in pattern.pattern.split('\s')]))
	
	return pattern