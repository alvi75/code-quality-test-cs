def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	with open(os.path.join(plugin_dir, 'plugin.yml'), 'r') as f:
		data = yaml.load(f)
	return data