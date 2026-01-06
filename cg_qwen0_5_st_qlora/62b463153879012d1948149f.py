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
	elif file_path.endswith(".docx") or file_path.endswith(".doc"):
		file_type = "docx"
	elif file_path.endswith(".xls") or file_path.endswith(".xlsx"):
		file_type = "xls"
	elif file_path.endswith(".ppt") or file_path.endswith(".pptx"):
		file_type = "ppt"
	else:
		return None

	if file_type == "pdf":
		component_id = file_path.split("/")[-1].split(".")[0]
		return {"component_id": component_id, "file_path": file_path}
	elif file_type == "docx" or file_type == "doc":
		component_id = file_path.split("/")[-1].split(".")[0]
		return {"component_id": component_id, "file_path": file_path, "ftype": "doc"}
	elif file_type == "xls" or file_type == "xlsx":
		component_id = file_path.split("/")[-1].split(".")[0]
		return {"component_id": component_id, "file_path": file_path, "ftype": "xls"}
	else:
		return None