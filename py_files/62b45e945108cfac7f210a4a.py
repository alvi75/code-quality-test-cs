def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""

	num_objects = 0
	good_objects = 0

	# Check for existence of required directories
	required_dirs = [self.dir_base,
					self.dir_data,
					self.dir_data + '/current',
					self.dir_data + '/current/meta']
	for d in required_dirs:
		if not os.path.isdir(d):
			raise Exception("Storage root '{}' does not exist.".format(d))

	# Check current meta file
	try:
		with open(self.dir_data + '/current/meta', 'r') as f:
			lines = f.readlines()
	except IOError:
		raise Exception("Storage root '{}' does not contain a current meta file.".format(self.dir_base))
	lines = [x.strip() for x in lines]
	if len(lines) == 0 or lines[0] != "storage_version: 1":
		raise Exception("Current meta file is invalid.")

	# Check for existence of previous meta files
	previous_meta_files = glob.glob(self.dir_data + "/current/meta.*")
	if len(previous_meta_files) > 1:
		raise Exception("More than one previous meta file exists.")

	# Check for existence of previous data files
	previous_data_files = glob.glob(self.dir_data + "/current/data.*")
	if len(previous_data_files) > 1:
		raise Exception("More than one previous data file exists.")

	# Check all object validity if requested
	if validate_objects:
		# Get list of all object hashes
		object_hashes = []
		for (dirpath, dirnames, filenames) in os.walk(self.dir_data + '/current'):
			for filename in filenames:
				if filename.endswith(".data"):
					object_hashes.append(filename[:-len('.data')])
		# Check each object hash
		for object_hash in object_hashes:
			num_objects += 1
			if self.validate_object(object_hash, check_digests=check_digests, show_warnings=show_warnings):
				good_objects += 1
			else:
				print("Warning: Object {} is corrupt.".format(object_hash))
	return num_objects, good_objects