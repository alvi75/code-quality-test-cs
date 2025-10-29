def _eval_file(prefix, file_path):
	"""
	Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".
	"""
	if not os.path.exists(file_path):
		return None

	file_type = None
	component_id = None
	if file_path.endswith(".pdf"):
		file_type = "pdf"
	elif file_path.endswith(".xml"):
		file_type = "xml"
	else:
		file_type = "other"

	with open(file_path) as f:
		for line in f:
			line = line.strip()
			if line.startswith("component_id:"):
				component_id = line.split(":")[1].strip()
			elif line.startswith("file_path:"):
				file_path = line.split(":")[1].strip()

	if file_type == "pdf":
		return {"component_id": component_id, "file_path": file_path}
	elif file_type == "xml":
		return {"component_id": component_id, "file_path": file_path, "ftype": file_type, "file_path": file_path}