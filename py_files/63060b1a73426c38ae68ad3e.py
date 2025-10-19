def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	spec = {}
	spec['name'] = os.path.basename(os.path.normpath(plugin_dir))
	spec['description'] = ''
	spec['version'] = '0.0.1'
	spec['author'] = ''
	spec['license'] = ''
	spec['url'] = ''
	spec['plugin_type'] = ''

	# Read the main yaml file
	if os.path.isfile(os.path.join(plugin_dir, 'plugin.yaml')):
		with open(os.path.join(plugin_dir, 'plugin.yaml'), 'r') as f:
			try:
				spec.update(yaml.load(f))
			except Exception as e:
				print('Error while parsing YAML file: %s' % str(e))

	return spec