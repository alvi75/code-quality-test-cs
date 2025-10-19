def match_file_by_prefix(prefix, file_path):
	"""
	Given a filepath, return true if the basename of the filepath is startswith the given prefix plus "-" or the given prefix plus "." 
	"""
	if not os.path.basename(file_path).startswith(prefix + "-") and not os.path.basename(file_path).startswith(prefix + "."):
		return False

	return True