def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	# TODO: This is a hack to get around the fact that the zipfile module doesn't support
	# iteration over nested directories, so we have to do this manually here.
	#
	# TODO: We should probably just be able to use os.walk() instead of iterating through
	# all files in the directory, but I'm not sure how much overhead it will add.

	def group_func(path, dir_or_file):
		if dir_or_file:
			return (path,)
		else:
			return ()

	files = []
	for root, dirs, files in os.walk(zip_path):
		for f in files:
			f = os.path.join(root, f)
			files.append(f)

	groups = [group_func(p, True) for p in files]
	# TODO: This is a hack to make the list comprehension work properly.
	# It's probably better to just return [(p,) for p in files] instead.
	return [(f,) for f in groups]