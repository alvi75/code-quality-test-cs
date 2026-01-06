def get_pattern(pattern, strip=True):
	"""
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""
	if isinstance(pattern, str):
		pattern = re.compile(pattern)
	elif not isinstance(pattern, re.Pattern):
		raise TypeError("pattern must be a string or a re.Pattern")
	if strip:
		pattern = pattern.sub(r'\1', pattern).strip()
	return pattern