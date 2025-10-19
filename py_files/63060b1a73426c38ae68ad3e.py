def get_yaml_file_contents(file_path, encoding='utf-8'):
		"""
		Reads a file from file_path and returns its contents as a string.
		"""
		with open(file_path, 'r', encoding=encoding) as f:
			return f.read()

	# Get the yaml file for this plugin
	yaml_file = os.path.join(plugin_dir, 'plugin.yml')
	if not os.path.exists(yaml_file):
		raise Exception('Plugin directory does not contain a plugin.yml file')

	# Read the yaml file
	yaml_contents = get_yaml_file_contents(yaml_file)

	# Parse the yaml file into a dictionary
	yaml_dict = yaml.load(yaml_contents)
	return yaml_dict