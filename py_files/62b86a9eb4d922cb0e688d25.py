def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"node": r"^[a-zA-Z0-9-_]{1,32}$",
		"edge": r"^[a-zA-Z0-9-_]{1,32}$",
		"graph": r"^[a-zA-Z0-9-_]{1,32}$",
	}