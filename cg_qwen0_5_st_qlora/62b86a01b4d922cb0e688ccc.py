def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	new_dict = {}
	for key in manifest_dict:
		if isinstance(manifest_dict[key], dict):
			new_dict[key] = generate_default_observer_schema_dict(manifest_dict[key], first_level=True)
		elif isinstance(manifest_dict[key], list):
			new_dict[key] = generate_default_observer_schema_list(manifest_dict[key])
		else:
			new_dict[key] = manifest_dict[key]
	return new_dict