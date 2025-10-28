def match_file_by_prefix(prefix, file_path):
	"""
	Given a filepath, return true if the basename of the filepath is startswith the given prefix plus "-" or the given prefix plus ".".
	"""
	if not os.path.isfile(file_path):
		return False

	file_name = os.path.basename(file_path)
	prefix_len = len(prefix)

	if file_name.startswith(prefix + "-"):
		return True
	elif file_name.startswith(prefix + "."):
		return True
	else:
		return False