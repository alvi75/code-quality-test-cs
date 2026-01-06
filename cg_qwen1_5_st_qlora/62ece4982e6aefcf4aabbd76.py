def match(filename):
	"""
	Check if the type of the given filename is 'doxyfile'

    Args:
        filename: filename to be check
    Returns:
        Return True if the type of the given filename in lower case is 'doxyfile'
	"""

	if not isinstance(filename, str):
		return False

	filename = filename.lower()
	return (filename == DOXYFILE) or (filename.endswith(DOXYFILE))