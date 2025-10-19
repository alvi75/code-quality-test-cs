def list_of_file_names(settings_dirs, spec_option):
	"""
	Create and return a new IniType complex type via cli.ListOfFileNames()
	"""
	return cli.ListOfFileNames(
		spec_option,
		[os.path.join(d, 'config.ini') for d in settings_dirs]
	)