def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

	Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	
	num_objects = 0
	good_objects = 0
	
	for obj in self.hierarchy:
		if obj.is_valid:
			good_objects += 1
		else:
			if not show_warnings:
				continue
			
			warning_message = "Object {} is invalid.".format(obj.path)
			if check_digests:
				warning_message += "\nCheck for object digest mismatch."
			
			self._warnings.append(Warning(warning_message))
		
		num_objects += 1
		
	return num_objects, good_objects