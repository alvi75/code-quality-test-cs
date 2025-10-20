def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if not os.path.exists(file_path):
		return None

	file_type = None
	component_id = None
	fpath = None
	with open(file_path) as f:
		for line in f:
			line = line.strip()
			if line.startswith(prefix + ''):
				component_id = line[len(prefix):]
				continue
			elif line.startswith('file_type:'):
				file_type = line[len('file_type:'):]
				continue
			elif line.startswith('fpath:'):
				fpath = line[len('fpath:'):]
				continue
			else:
				continue
		if file_type == 'pdf':
			return {'component_id': component_id, 'file_path': fpath}
		elif file_type != 'xml':
			return None
		else:
			return {'component_id': component_id, 'file_path': fpath, 'ftype': file_type, 'file_path': fpath}