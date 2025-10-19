def get_pattern(pattern, strip=True):
	"""
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""

	if isinstance(pattern, Pattern):
		return pattern
	elif isinstance(pattern, str):

		pattern = re.sub(r'(^ +)(.+)( +$)', r'\2', pattern)  # remove leading/trailing spaces
		if strip:
			pattern = pattern.strip()

		return re.compile(pattern)
	else:
		raise TypeError('pattern must be of type str or Pattern')