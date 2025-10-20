def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	for arg in cli_args:
		if arg in answer_file_args:
			print("Argument '%s' is deprecated" % arg)
			print("Please use '%s' instead." % answer_file_args[arg])