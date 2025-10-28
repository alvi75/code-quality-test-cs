def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	if first_level:
		return manifest_dict

	default_dict = {}
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			default_dict[key] = generate_default_observer_schema_dict(value)
		elif isinstance(value, list):
			default_dict[key] = [generate_default_observer_schema_dict(item) for item in value]
		else:
			default_dict[key] = value
	return default_dict