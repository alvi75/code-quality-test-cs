def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	return {k: v for k, v in six.iteritems(inventory) if k.startswith(version)}