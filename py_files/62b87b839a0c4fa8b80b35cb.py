def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	errs = self._err_dict[coord_name]
	return [i for i in range(len(errs)) if errs[i] > 0]