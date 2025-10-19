def _generate_default_observers_schema_dict(manifest_dict, key, schema_type, default_value=None):
		if isinstance(schema_type, list):
			for item in schema_type:
				yield _generate_default_observers_schema_dict(manifest_dict, key, item)
		elif isinstance(schema_type, dict):
			for k, v in schema_type.items():
				yield _generate_default_observers_schema_dict(manifest_dict, "%s.%s" % (key, k), v)
		else:
			yield _generate_default_observers_schema_dict(manifest_dict, key, schema_type, default_value)

	return {k: _generate_default_observers_schema_dict(manifest_dict, k, v) for k, v in manifest_dict.items()}