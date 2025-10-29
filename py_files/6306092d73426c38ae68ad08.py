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

	required_when = self._get_required_when(options_spec)
	return [arg for arg in args if self._is_required_when_matched(
			command_name, required_when, arg)]