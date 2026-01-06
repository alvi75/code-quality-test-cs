def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""

	if self.deprecated_arguments is None:
		return

	for arg in self.deprecated_arguments.keys():
		if arg in cli_args or arg in answer_file_args:
			print("WARNING: The argument '{}' has been deprecated.".format(arg))