def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	spec = {}
	for filename in os.listdir(plugin_dir):
		if filename.endswith('.yaml'):
			with open(os.path.join(plugin_dir, filename), 'r') as f:
				spec.update(yaml.load(f))
	return spec