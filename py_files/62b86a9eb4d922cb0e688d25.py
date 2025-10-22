def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"cluster": r"^[\w\-]+$",
		"node": r"^[\w\-]+$",
		"service": r"^[\w\-]+$",
		"deployment": r"^[\w\-]+$",
		"configmap": r"^[\w\-]+$",
		"secret": r"^[\w\-]+$",
		"ingress": r"^[\w\-]+$",
		"route53": r"^[\w\-]+$",
	}