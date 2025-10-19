def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	return [i for i in range(len(self.coord_names)) if self.coord_names[i] == coord_name]