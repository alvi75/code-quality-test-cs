def get_pattern(pattern, strip=True):
	"""
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""
	if isinstance(pattern, re.Pattern):
		return pattern
	else:
		pattern = pattern.strip()
		if strip:
			pattern = pattern.strip()
		return re.compile(pattern)