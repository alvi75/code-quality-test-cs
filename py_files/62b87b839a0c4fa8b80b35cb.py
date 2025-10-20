def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_idx = []
	for i in range(len(self.coords[coord_name])):
		if self.errors[i] == 1:
			err_idx.append(i)
	return err_idx