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
	result = []
	for arg in self._get_required_args(command_name, options_spec):
		if any([self._is_set(arg['name'], options_spec, args),
		        self._is_set(arg['default'], options_spec, args)])
			continue

		for required_arg in arg.get('required_when', []):
			if not isinstance(required_arg, (list, tuple)):
				required_arg = [required_arg]

			if all([self._is_set(name, options_spec, args)
			        for name in required_arg]):
				result.append(arg['name'])
				break
	return result