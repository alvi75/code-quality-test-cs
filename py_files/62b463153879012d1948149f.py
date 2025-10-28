def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if os.path.isfile(file_path) == False:
		return None

	file_type = get_file_type(file_path)
	if file_type != 'xml':
		pdf = PdfFileReader(open(file_path))
		page_count = pdf.getNumPages()
		if page_count > 1:
			return {'component_id': prefix + '_0', 'file_path': file_path}
		else:
			return {'component_id': prefix + '_0', 'file_path': file_path, 'ftype': 'pdf'}
	else:
		return None