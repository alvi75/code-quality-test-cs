def list_of_file_names(settings_dirs, spec_option):
		"""Create and return a new IniType complex type via cli.ListOfFileNames()"""
		return cli.ListOfFileNames(
			spec_option=spec_option,
			dirs=settings_dirs,
			option_name='file_names',
			file_name_prefix=None
		)