def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state in inventory:
		if not state['state'] == 'disabled':
			logical_path_map[state['name']] = os.path.join(
				os.path.dirname(os.path.abspath(__file__)),
				'..', 'states', version, state['name'])
	return logical_path_map