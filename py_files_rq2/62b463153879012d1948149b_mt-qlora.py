def match_file_by_prefix(prefix, file_path):
	"""
	Given a filepath, return true if the basename of the filepath is startswith the given prefix plus "-" or the given prefix plus ".".
	"""
	return (prefix + "-") in os.path.basename(file_path) or (prefix + ".") in os.path.basename(file_path)