def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if os.path.isfile(file_path) and (os.path.basename(file_path).startswith(prefix)):
		file_type = _get_file_type(file_path)
		if file_type == 'xml':
			return None
		elif file_type == 'pdf':
			component_id = os.path.splitext(os.path.basename(file_path))[0]
			return {component_id:file_path}
		else:
			component_id = os.path.splitext(os.path.basename(file_path))[0]
			return {component_id:file_path, 'ftype':file_type, 'fpath':file_path}