def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
	"""
	Runs ansible cli with vars dict

:param vars_dict: dict, Will be passed as Ansible extra-vars
:param cli_args: the list  of command line arguments
:param ir_workspace: An Infrared Workspace object represents the active
 workspace
:param ir_plugin: An InfraredPlugin object of the current plugin
:return: ansible results
	"""

	if not isinstance(vars_dict, dict):
		raise ValueError("vars_dict must be a dictionary")

	if not isinstance(cli_args, list):
		raise ValueError("cli_args must be a list")

	if not isinstance(ir_workspace, Workspace):
		raise ValueError("ir_workspace must be a Workspace object")

	if not isinstance(ir_plugin, InfraredPlugin):
		raise ValueError("ir_plugin must be an InfraredPlugin object")

	# Create the ansible inventory file
	inventory = _create_inventory_file(cli_args, ir_workspace)

	# Create the ansible playbook file
	playbook = _create_playbook_file(cli_args, ir_workspace, ir_plugin)

	# Create the ansible inventory file
	# inventory = _create_inventory_file(cli_args, ir_workspace)
	# Create the ansible playbook file
	# playbook = _create_playbook_file(cli_args, ir_workspace, ir_plugin)

	# Run the ansible playbook
	return _run_ansible_cli(playbook, inventory, vars_dict)