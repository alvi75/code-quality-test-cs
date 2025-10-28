def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_ind = []
	for i in range(len(self._err_data)):
		if self._err_data[i][0] == coord_name:
			err_ind.append(i)
	return err_ind