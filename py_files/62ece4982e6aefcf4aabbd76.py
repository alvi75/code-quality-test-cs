def match(filename):
	"""
	Check if the type of the given filename is 'doxyfile'

    Args:
        filename: filename to be check
    Returns:
        Return True if the type of the given filename in lower case is 'doxyfile'
	"""

	if not os.path.isfile(filename):
		return False

	filename = filename.lower()
	return filename.endswith('.doxyfile') or filename.endswith('.Doxyfile')