def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if os.path.isfile(file_path) == False:
		return None

	file_type = get_file_type(file_path)
	if file_type != 'pdf':
		return None

	component_id = os.path.basename(file_path).split('.')[0]
	pdf_dict = {'component_id': component_id,
				'file_path': file_path}
	return pdf_dict