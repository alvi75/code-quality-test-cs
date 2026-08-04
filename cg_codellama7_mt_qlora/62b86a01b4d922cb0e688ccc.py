def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	new_dict = {}
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			new_dict[key] = generate_default_observer_schema_dict(value, first_level=False)
		elif isinstance(value, list):
			new_dict[key] = []
		elif isinstance(value, str):
			new_dict[key] = value
		else:
			raise ValueError("The value type of the key {} is not supported.".format(key))
	if first_level:
		new_dict = {"observer_schema": new_dict}
	return new_dict