def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	if not isinstance(manifest_dict, dict):
		raise TypeError("The argument 'manifest_dict' must be a dictionary.")
	if not isinstance(first_level, bool):
		raise TypeError("The argument 'first_level' must be a boolean.")
	new_dict = {}
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			new_dict[key] = generate_default_observer_schema_dict(value, first_level)
		elif isinstance(value, list):
			new_dict[key] = [generate_default_observer_schema_dict(item, first_level) for item in value]
		else:
			new_dict[key] = value
	return new_dict