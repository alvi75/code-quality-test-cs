def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state_name in inventory:
		if not os.path.exists(os.path.join(state_dir, state_name)):
			raise Exception("State %s does not exist" % state_name)
		logical_path_map[state_name] = os.path.join(state_dir, state_name)
	return logical_path_map