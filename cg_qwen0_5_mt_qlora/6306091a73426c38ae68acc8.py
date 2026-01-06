def list_of_file_names(settings_dirs, spec_option):
	"""
	Create and return a new IniType complex type via cli.ListOfFileNames()
	"""
	return ComplexType(
		"listOfFileNames",
		{
			"settingsDirs": settings_dirs,
			"specOption": spec_option,
		},
	)