def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state in inventory.states:
		if state.version == version:
			logical_path_map[state.logical_path] = state.path
	return logical_path_map