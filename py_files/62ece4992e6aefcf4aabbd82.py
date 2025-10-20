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
		raise ValueError("pattern must be a string or compiled regex")

	if strip:
		return pattern.strip()
	else:
		return pattern