def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state_name in inventory:
		if not isinstance(inventory[state_name], list):
			continue

		for state in inventory[state_name]:
			if not isinstance(state, dict):
				continue

			if 'path' in state:
				logical_path_map[state['name']] = state['path']
			else:
				logical_path_map[state['name']] = os.path.join(version, state['name'])

	return logical_path_map