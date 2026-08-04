def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec_file = os.path.join(plugin_dir, 'plugin_spec.yaml')
	if not os.path.exists(plugin_spec_file):
		return {}
	with open(plugin_spec_file, 'r') as f:
		plugin_spec = yaml.load(f)
	return plugin_spec