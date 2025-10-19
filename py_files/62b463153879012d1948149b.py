def match_file_by_prefix(prefix, file_path):
		if not os.path.exists(file_path) or not os.path.isfile(file_path):
			return False

		file_basename = os.path.basename(file_path)
		return (file_basename.startswith(prefix + "-") or file_basename.startswith(prefix + ".")) and \
			   (not file_basename.endswith(".pyc") or not file_basename.endswith(".pyo"))