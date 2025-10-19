def get_pattern(pattern, strip=True):
    """
	Convert a string to a regex pattern object

    Args:
            pattern: str or regex pattern object
            strip: boolean, whether the spaces in the start/end will be stripped
    Returns:
            regex pattern object
	"""

    if isinstance(pattern, six.string_types):
        return re.compile(r'^' + re.sub(r'\s+', '', pattern) + r'$')
    else:
        return pattern