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
		if arg not in self._args:
			continue

		arg_options = options_spec.get(arg)
		if arg_options is None or 'required_when' not in arg_options:
			continue

		if eval(arg_options['required_when'], {}, {}) == True:
			required_args.append(arg)

	return required_args