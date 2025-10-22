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
	if not vars_dict:
		vars_dict = {}
	# Add the default vars to the vars_dict
	for key in DEFAULT_VARS:
		if key not in vars_dict:
			vars_dict[key] = DEFAULT_VARS[key]
	# Add the workspace vars to the vars_dict
	for key in ir_workspace.get_vars():
		if key not in vars_dict:
			vars_dict[key] = ir_workspace.get_var(key)
	# Add the plugin vars to the vars_dict
	for key in ir_plugin.get_vars():
		if key not in vars_dict:
			vars_dict[key] = ir_plugin.get_var(key)

	# Add the playbook name to the vars_dict
	playbook_name = ir_plugin.get_playbook()
	if playbook_name is None:
		raise Exception("Playbook name is not defined")
	vars_dict['playbook'] = playbook_name

	# Add the inventory file to the vars_dict
	inventory_file = ir_workspace.get_inventory_file()
	if inventory_file is None:
		raise Exception("Inventory file is not defined")
	vars_dict['inventory'] = inventory_file

	# Add the hostfile to the vars_dict
	hostfile = ir_workspace.get_hostfile()
	if hostfile is not None:
		vars_dict['hostfile'] = hostfile

	# Add the connection type to the vars_dict
	connection_type = ir_workspace.get_connection_type()
	if connection_type is not None:
		vars_dict['connection'] = connection_type

	# Add the module args to the vars_dict
	module_args = ir_plugin.get_module_args()
	if module_args is not None:
		vars_dict['module_args'] = module_args

	# Add the module to the vars_dict
	module = ir_plugin.get_module()
	if module is not None:
		vars_dict['module'] = module

	# Add the module options to the vars_dict
	module_options = ir_plugin.get_module_options()
	if module_options is not None:
		vars_dict['module_opts'] = module_options

	# Add the module options to the vars_dict