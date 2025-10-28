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
	for arg in options_spec:
		if 'required_when' not in arg:
			continue

		arg_name = arg['name']
		value = self._get_arg_value(command_name, arg_name, args)
		if value is None:
			continue

		if self._is_match(arg['required_when'], value):
			required_args.append(arg_name)

	return required_args