def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"cluster": re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"),
		"node": re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"),
		"service": re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"),
		"pod": re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"),
	}