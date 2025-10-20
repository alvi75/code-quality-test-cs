def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	default_observer_schema_dict = {}
	for key in manifest_dict:
		if isinstance(manifest_dict[key], dict):
			default_observer_schema_dict[key] = generate_default_observer_schema_dict(manifest_dict[key])
		elif isinstance(manifest_dict[key], list):
			default_observer_schema_dict[key] = []
			for item in manifest_dict[key]:
				if isinstance(item, dict):
					default_observer_schema_dict[key].append(generate_default_observer_schema_dict(item))
				else:
					default_observer_schema_dict[key].append(item)
		else:
			default_observer_schema_dict[key] = None
	return default_observer_schema_dict