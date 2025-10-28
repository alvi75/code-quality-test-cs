def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	for arg in self.deprecated_arguments:
		if arg in cli_args:
			print("Warning: The argument '%s' is deprecated. "
				"Please use '%s' instead." % (arg, self.deprecated_arguments[arg]))
		elif arg in answer_file_args:
			print("Warning: The argument '%s' is deprecated. "
				"Please use '%s' instead." % (arg, self.deprecated_arguments[arg]))