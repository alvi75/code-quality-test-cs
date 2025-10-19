def validate_storage_root(storage_root, validate_objects=True, check_digests=True, show_warnings=False):
	"""
	Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
	"""
	num_objects = 0
	good_objects = 0

	for path in os.listdir(storage_root):
		if not path.startswith('.'):
			path = os.path.join(storage_root, path)
			try:
				file_info = os.stat(path)
			except OSError as e:
				if e.errno == errno.ENOENT:
					pass
				else:
					raise
			else:
				num_objects += 1
				if validate_objects:
					if file_info.st_size > 0:
						if check_digests:
							digest = hashlib.md5()
							with open(path, 'rb') as f:
								digest.update(f.read())
							if digest.hexdigest() != file_info.st_ino:
								if show_warnings:
									warnings.warn("Object %s has inconsistent size" % (path,))
								continue
					good_objects += 1

	return num_objects, good_objects