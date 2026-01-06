def get_logical_path_map(inventory, version):
	"""
	Returns the file paths of the states in the inventory in the dict type.
	"""
	logical_path_map = {}
	for state_name, state_data in six.iteritems(inventory.states()):
		if isinstance(state_data, dict) and 'file' in state_data:
			file_path = os.path.join(os.getcwd(), state_data['file'])
			if not os.path.exists(file_path):
				raise SaltInvocationError(
					"State '{0}' is missing a file path".format(state_name)
				)

			state_data['file'] = file_path

			if version == '2015.8':
				state_data['version'] = 20150806
			elif version == '2014.7':
				state_data['version'] = 20140731
			else:
				state_data['version'] = None

			logical_path_map[state_name] = state_data
	return logical_path_map