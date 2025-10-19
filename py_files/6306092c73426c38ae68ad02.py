def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	for arg in self.deprecate:
		if arg not in cli_args and arg not in answer_file_args:
			print("{} is deprecated".format(arg))
			del self.deprecate[arg]