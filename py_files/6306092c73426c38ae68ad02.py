def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	for arg in self.deprecated:
		if arg in cli_args:
			self.print_error("Argument '%s' is deprecated" % arg)
			self.print_error("Please use '%s' instead." % arg)
			self.print_error("See --help for more information.")
			return False

	for arg in self.deprecated:
		if arg in answer_file_args:
			self.print_error("Argument '%s' is deprecated" % arg)
			self.print_error("Please use '%s' instead." % arg)
			self.print_error("See --help for more information.")
			return False

	return True