def was_processed(processed, path_name, verbose):
	"""
	Check if a file or directory has already been processed.

    To prevent recursion, expand the path name to an absolution path
    call this function with a set that will store all the entries and
    the entry to test. If the entry is already in the set, report the issue
    and return ``True``. Otherwise, add the entry to the set and return
    ``False`` to allow the path to be processed.

    Args:
        processed: Set to store processed pathnames
        path_name: Path to a directory or file
        verbose: True if verbose output is requested

    Returns:
        True if it's already in the set. False if not.
	"""
	if os.path.isdir(path_name):
		path_name = os.path.abspath(path_name)
	else:
		path_name = os.path.dirname(os.path.abspath(path_name))

	if path_name in processed:
		if verbose:
			print("Skipping %s" % path_name)
		return True
	else:
		processed.add(path_name)
		return False