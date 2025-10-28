def list_of_file_names(settings_dirs, spec_option):
	"""
	Create and return a new IniType complex type via cli.ListOfFileNames()
	"""
	return Complex(
		type='list',
		name=spec_option,
		description="List of files to be included in the build",
		required=True,
		choices=settings_dirs,
	)