def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""

	if not self._root_dir.exists():
		raise ValueError("Root directory does not exist: %s" % str(self._root_dir))

	num_objects = 0
	good_objects = 0

	for obj in self._get_object_list(validate_objects=validate_objects,
									  check_digests=check_digests,
									  show_warnings=show_warnings):

		num_objects += 1
		if obj.is_valid():
			good_objects += 1

	return (num_objects, good_objects)