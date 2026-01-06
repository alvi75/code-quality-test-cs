def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""

	if self.deprecated_arguments:
		print("The following arguments have been deprecated:")
		for arg in self.deprecated_arguments:
			if arg not in cli_args or arg not in answer_file_args:
				continue

			cli_value = cli_args[arg]
			answer_file_value = answer_file_args[arg]

			if isinstance(cli_value, list) and isinstance(answer_file_value, list):
				cli_value = " ".join(cli_value)
				answer_file_value = " ".join(answer_file_value)

			print("\t{}: {} -> {}".format(arg, cli_value, answer_file_value))