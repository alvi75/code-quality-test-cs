def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	resource_name_regex = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9]*$')
	return resource_name_regex