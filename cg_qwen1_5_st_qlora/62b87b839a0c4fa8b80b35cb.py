def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	errs = []
	for i in range(len(self.coords)):
		if self.coords[i].name == coord_name:
			errs.append(i)
	return errs