def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	return [i for i in self._err_ind if self._err_ind[i][0] == coord_name]