def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_indices = []
	for i in range(len(self._err)):
		if self._err[i][0] == coord_name:
			err_indices.append(i)
	return err_indices