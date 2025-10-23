def _get_conditionally_required_args(self, command_name, options_spec,
                                        args):
	"""
	List arguments with ``required_when`` condition matched.

:param command_name: the command name.
:param options_spec:  the list of command spec options.
:param args: the received input arguments
:return: list, list of argument names with matched ``required_when``
    condition
	"""

	required_args = []
	for arg in args:
		if arg in options_spec:
			arg_spec = options_spec[arg]
			if 'required_when' in arg_spec:
				required_when = arg_spec['required_when']
				if required_when[0] in args and required_when[1] in args:
					required_args.append(arg)
	return required_args