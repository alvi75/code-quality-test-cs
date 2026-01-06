def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for obj in self.get_all_objects():
		if not obj.validate(validate_objects=validate_objects, check_digests=check_digests, show_warnings=show_warnings):
			self.log("Object %s is invalid" % obj)
		else:
			good_objects += 1

	return num_objects, good_objects