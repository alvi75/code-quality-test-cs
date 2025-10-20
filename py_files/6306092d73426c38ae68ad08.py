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
	condition = self._get_condition(command_name, options_spec)
	if not condition:
		return []
	kwargs = {}
	for arg in args:
		if arg['name'] in condition:
			kwargs[arg['name']] = arg
	return kwargs.keys()