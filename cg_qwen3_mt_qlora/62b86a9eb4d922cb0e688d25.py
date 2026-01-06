def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"agent": re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_\-]*$"),
		"device": re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_\-]*$"),
		"measurement": re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_\-]*$"),
		"metric": re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_\-]*$")
	}