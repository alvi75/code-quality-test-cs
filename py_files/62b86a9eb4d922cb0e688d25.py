def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"cluster": r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"node": r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"service": r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
	}