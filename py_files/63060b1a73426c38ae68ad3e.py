def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	with open(os.path.join(plugin_dir, 'plugin.yaml')) as f:
		spec = yaml.load(f)
	spec['name'] = os.path.basename(plugin_dir)
	return spec