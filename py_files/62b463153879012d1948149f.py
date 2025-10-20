def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if not os.path.isfile(file_path):
		return None

	file_name = os.path.basename(file_path)
	component_id = file_name.split('.')[0]

	if not file_name.startswith(prefix):
		return None

	if file_name.endswith('.xml'):
		return None

	if file_name.endswith('.pdf'):
		return {component_id: file_path}

	else:
		ftype = file_name.split('.')[-1]
		return {component_id: file_path, 'ftype': ftype}