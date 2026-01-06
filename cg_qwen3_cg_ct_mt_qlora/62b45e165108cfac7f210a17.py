def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state in inventory:
		if not state['state']:
			continue
		logical_path_map[state['state']] = os.path.join(
			version,
			state['state'],
			state['name']
		)
	return logical_path_map