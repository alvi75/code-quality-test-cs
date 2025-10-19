def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	lpm = {}
	for state in inventory:
		if isinstance(state, six.string_types) or isinstance(state, six.text_type):
			state = state.strip()
		else:
			raise TypeError("State is not a string")
		if state.startswith("/"):
			lpm[state] = state
		elif state.startswith("../"):
			lpm[state] = os.path.join(os.path.dirname(lpm[""]), state)
		else:
			lpm[state] = os.path.join(version, state)

	return lpm