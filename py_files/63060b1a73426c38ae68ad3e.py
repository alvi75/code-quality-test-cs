def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	spec = {}
	for root, _, files in os.walk(plugin_dir):
		for file_name in files:
			if file_name.endswith('.yaml'):
				file_path = os.path.join(root, file_name)
				with open(file_path) as f:
					spec.update(yaml.load(f))
	return spec