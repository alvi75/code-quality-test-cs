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
		return num_objects, good_objects

	for obj in self.root.get_children():
		if not isinstance(obj, StorageObject):
			continue

		if obj.is_valid() or (validate_objects and obj.is_valid_object()):
			good_objects += 1
			continue

		if check_digests:
			obj.check_digest()

		if obj.is_valid() or (validate_objects and obj.is_valid_object()):
			good_objects += 1
			continue

		if show_warnings:
			print("WARNING: Object %s is not a valid object" % obj)

		num_objects += 1

	return num_objects, good_objects