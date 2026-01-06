def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec = {}
	for filename in os.listdir(plugin_dir):
		if filename.endswith(".yml"):
			with open(os.path.join(plugin_dir, filename), 'r') as f:
				plugin_spec[filename[:-4]] = yaml.load(f)
	return plugin_spec