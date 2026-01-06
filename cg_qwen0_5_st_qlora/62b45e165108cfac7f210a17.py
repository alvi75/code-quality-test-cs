def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	return {state: os.path.join(
			inventory['path'], state, 'states', version,
			'__init__.py') for state in inventory['states']}