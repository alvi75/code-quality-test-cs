def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	if self.root is None:
		return (num_objects, good_objects)

	for obj in self.root.get_children():
		num_objects += 1
		try:
			obj.validate(check_digests=check_digests)
			good_objects += 1
		except Exception as e:
			if show_warnings:
				print("WARNING: %s" % str(e))
			continue

	return (num_objects, good_objects)