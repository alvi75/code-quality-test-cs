def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	deprecated_args = self.get_deprecated_args()
	for arg in deprecated_args:
		if arg in cli_args:
			print_warning("Argument '%s' is deprecated and will be removed in the next release. Please use '%s' instead." % (arg, deprecated_args[arg]))
		elif arg in answer_file_args:
			print_warning("Argument '%s' is deprecated and will be removed in the next release. Please use '%s' instead." % (arg, deprecated_args[arg]))