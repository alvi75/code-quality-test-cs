def match(filename):
	"""
	Check if the type of the given filename is 'doxyfile'

    Args:
        filename: filename to be check
    Returns:
        Return True if the type of the given filename in lower case is 'doxyfile'
	"""
	return os.path.splitext(os.path.basename(filename))[1].lower() == '.doxyfile'