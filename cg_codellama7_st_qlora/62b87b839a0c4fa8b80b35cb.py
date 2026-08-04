def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_indices = []
	for i, coord in enumerate(self.coords):
		if coord.name == coord_name:
			err_indices.append(i)
	return err_indices