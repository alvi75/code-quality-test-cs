def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if not os.path.exists(file_path):
		return None

	file_type = None
	component_id = None
	for component in COMPONENTS:
		if file_path.endswith(component + '.pdf'):
			component_id = component
			file_type = 'pdf'
			break

	if file_type == 'pdf':
		return {'component_id': component_id, 'file_path': file_path}
	else:
		return None