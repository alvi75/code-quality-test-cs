def validate_arg_deprecation(self, cli_args, answer_file_args):
	"""
	Validates and prints the deprecated arguments.

:param cli_args: the dict of arguments from cli
:param answer_file_args:  the dict of arguments from files
	"""
	if 'answer' in cli_args or 'answer_file' in cli_args:
		self.printer('\nWarning: The --answer and --answer-file options have been deprecated.\n'
					 'Please use --yes and --yes-file instead.')
		if 'answer' in cli_args:
			answer_file_args['answer'] = cli_args['answer']
			del cli_args['answer']
		if 'answer_file' in cli_args:
			answer_file_args['answer_file'] = cli_args['answer_file']
			del cli_args['answer_file']