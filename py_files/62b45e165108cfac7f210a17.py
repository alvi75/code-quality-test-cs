def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	path_map = {}
	for state in sorted(inventory['states']):
		path_map[state] = os.path.join(
			inventory['states'][state]['path'], 
			inventory['states'][state]['file']
		)
	return path_map