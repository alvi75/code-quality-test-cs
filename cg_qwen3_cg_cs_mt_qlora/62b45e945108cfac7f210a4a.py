def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for obj in self.objects.values():
		if not obj.is_valid():
			if show_warnings:
				print("Warning: Object %s is invalid" % obj.name)
		else:
			good_objects += 1
		num_objects += 1

	return num_objects, good_objects