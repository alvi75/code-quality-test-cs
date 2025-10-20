def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for obj in self.root.get_all_objects():
		if not obj.is_valid():
			continue

		if validate_objects:
			obj.validate()

		if check_digests:
			obj.check_digest()

		if show_warnings:
			print("Validating %s" % obj)

		good_objects += 1
		num_objects += 1

	return num_objects, good_objects