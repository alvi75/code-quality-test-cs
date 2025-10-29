def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for obj in self.objects():
		if not obj.is_valid():
			if show_warnings:
				print("Warning: Object %s is invalid" % obj)
			continue

		if validate_objects:
			if not obj.validate(show_warnings=show_warnings):
				if show_warnings:
					print("Warning: Object %s failed validation" % obj)
				continue

		if check_digests:
			if not obj.check_digests():
				if show_warnings:
					print("Warning: Object %s has bad digests" % obj)
				continue

		num_objects += 1
		good_objects += 1

	return num_objects, good_objects