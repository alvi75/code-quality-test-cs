def get_pattern(pattern, strip=True):
	"""
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""
	if isinstance(pattern, re._pattern_type):
		return pattern
	elif isinstance(pattern, str):
		pattern = pattern.strip()
		if strip else pattern
		return re.compile(pattern)
	else:
		raise ValueError("Pattern must be either a string or a regex pattern")