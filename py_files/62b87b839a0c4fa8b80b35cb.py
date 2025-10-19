def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_names = self._error_names
	if not err_names:
		return []
	err_indices = set()
	for i, name in enumerate(err_names):
		if name == coord_name:
			err_indices.add(i)
	return list(err_indices)