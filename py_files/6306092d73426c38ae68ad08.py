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
		if isinstance(arg, dict) and 'name' in arg:
			name = arg['name']
			if self._is_argument(name, options_spec):
				command_option = self._find_command_option(command_name,
																options_spec)
				if not command_option:
					raise CommandError('Command %s is unknown.' %
											command_name)

				if not command_option.get('required', False):
					continue

				if not self._check_required_conditions(name, command_option,
														arg):
					raise CommandError(
						'%s is required by command %s.' % (name, command_name))

				required_args.append(name)
	return required_args