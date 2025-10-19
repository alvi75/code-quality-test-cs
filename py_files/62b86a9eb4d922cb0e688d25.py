def _get_resource_name_regex():
		"""
		Return the regular expressions that are used to validate the name of the Krake resources
		"""
		return re.compile(r'^[A-Za-z0-9_\-]{1,63}$', re.IGNORECASE)

	return _get_resource_name_regex