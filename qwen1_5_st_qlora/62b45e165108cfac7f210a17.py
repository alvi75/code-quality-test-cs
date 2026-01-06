def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	return {state: os.path.join(os.getcwd(), state) for state in inventory.get_states(version)}