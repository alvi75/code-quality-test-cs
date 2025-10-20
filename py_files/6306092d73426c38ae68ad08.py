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
		if option['name'] not in args:
			continue

		if 'required_when' not in option:
			continue

		# check if all required_when conditions are met
		matched = True
		for cond in option['required_when']:
			if cond[0] == 'not':
				if cond[1] in args:
					matched = False
					break
			else:
				if cond[1] not in args:
					matched = False
					break

		if matched:
			required_when.append(option['name'])

	return required_when