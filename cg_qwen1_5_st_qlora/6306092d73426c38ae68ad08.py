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
	for arg in self._args:
		if not isinstance(arg, Option):
			continue

		arg_name = arg.name
		if arg.required_when is None or \
				not arg.required_when.match(command_name, args):
			continue

		required_args.append(arg_name)

	return required_args