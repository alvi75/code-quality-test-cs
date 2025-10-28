def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for obj in self.root.objects:
		if not obj.is_valid():
			self._log("Object %s is invalid" % obj)
			continue

		if validate_objects:
			try:
				obj.validate()
			except Exception as e:
				self._log("Object %s validation failed: %s" % (obj, str(e)))
				continue

		if check_digests:
			try:
				obj.check_digest()
			except Exception as e:
				self._log("Object %s digest check failed: %s" % (obj, str(e)))
				continue

		if obj.is_root:
			continue

		if not obj.is_valid():
			self._log("Object %s is invalid" % obj)
			continue

		if validate_objects:
			try:
				obj.validate()
			except Exception as e:
				self._log("Object %s validation failed: %s" % (obj, str(e)))
				continue

		if check_digests:
			try:
				obj.check_digest()
			except Exception as e:
				self._log("Object %s digest check failed: %s" % (obj, str(e)))
				continue

		num_objects += 1
		good_objects += 1

	return num_objects, good_objects