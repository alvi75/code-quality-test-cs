def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	if not isinstance(manifest_dict, dict):
		raise TypeError("manifest_dict must be a dict")
	new_dict = {}
	for key, value in manifest_dict.items():
		if key == 'schema':
			continue
		elif key == 'name' or key == 'description':
			value = str(value)
		elif key == 'type':
			value = _generate_type_schema_dict(value)
		elif key == 'default':
			value = _generate_default_schema_dict(value)
		elif key == 'enum':
			value = _generate_enum_schema_dict(value)
		elif key == 'items':
			value = _generate_items_schema_dict(value)
		elif key == 'properties':
			value = _generate_properties_schema_dict(value)
		elif key == 'required':
			value = _generate_required_schema_dict(value)
		else:
			value = _generate_value_schema_dict(value)

		if first_level:
			new_dict[key] = value
		else:
			new_dict['properties'][key] = value

	return new_dict