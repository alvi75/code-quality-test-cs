def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""

	if not isinstance(manifest_dict, dict):
		raise TypeError("manifest_dict must be a dict")

	new_dict = {}
	for key, value in manifest_dict.items():
		if key == "type":
			continue

		if key == "schema" or key == "default":
			value = json.loads(value)

		if isinstance(value, dict):
			value = generate_default_observer_schema_dict(value)
		elif isinstance(value, list):
			value = [generate_default_observer_schema_dict(item) for item in value]
		else:
			pass

		new_dict[key] = value

	return new_dict