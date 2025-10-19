def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	new_dict = {}
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			new_dict[key] = generate_default_observer_schema_dict(value)
		elif isinstance(value, list):
			new_dict[key] = [generate_default_observer_schema_dict(item) for item in value]
		else:
			new_dict[key] = value

	if not first_level:
		return new_dict
	else:
		return generate_default_observer_schema_dict(new_dict, True)