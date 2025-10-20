def get_nested_custom_and_control_args(self, args):
	"""
	Split input arguments to control nested and custom.

Controls arguments: control the IR behavior. These arguments
    will not be put into the spec yml file
Nested arguments: are used by the Ansible playbooks and will be put
    into the spec yml file.
Custom arguments: Custom ansible variables to be used instead of the
    normal nested usage.

:param args: the collected list of args.
:return: (dict, dict): flat dicts (control_args, nested_args)
	"""

	control_args = {}
	nested_args = {}

	for arg in args:
		if arg.startswith("--"):
			key, value = arg.split("=", 1)

			if key == "--nested":
				nested_args["ansible_nest_level"] = int(value)
			elif key == "--custom":
				custom_key, custom_value = value.split("=", 1)
				nested_args[custom_key] = custom_value

		else:
			control_args[arg] = True

	return control_args, nested_args