def list_of_file_names(settings_dirs, spec_option):
	"""
	Create and return a new IniType complex type via cli.ListOfFileNames()
	"""
	return cli.ListOfFileNames(
		settings_dirs,
		spec_option,
		default=None,
		help="List of file names to be used as input for the analysis",
		metavar="FILENAME",
		nargs="+",
		type=str,
	)