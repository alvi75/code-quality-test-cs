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
	required_when = []
	for option in options_spec:
		if option['name'] == command_name:
			for arg in option.get('args', []):
				if arg.get('required_when'):
					required_when.extend(arg['required_when'])
	return required_when