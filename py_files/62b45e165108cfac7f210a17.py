def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state in inventory:
		state_name = state['name']
		if state_name not in logical_path_map:
			logical_path_map[state_name] = []
		logical_path_map[state_name].append(state)
	return logical_path_map