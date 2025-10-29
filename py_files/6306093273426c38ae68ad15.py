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

	if not ir_workspace:
		raise Exception("No workspace is set")

	if not ir_plugin:
		raise Exception("No plugin is set")

	# Set up the inventory file
	inventory_file = os.path.join(ir_workspace.get_path(), 'inventory')
	with open(inventory_file, 'w') as f:
		f.write(ir_workspace.get_inventory())

	# Set up the playbook file
	playbook_file = os.path.join(ir_workspace.get_path(), 'playbook.yml')
	with open(playbook_file, 'w') as f:
		f.write(ir_workspace.get_playbook())

	# Set up the hosts file
	hosts_file = os.path.join(ir_workspace.get_path(), 'hosts')
	with open(hosts_file, 'w') as f:
		f.write(ir_workspace.get_hosts())

	# Set up the group_vars file
	group_vars_file = os.path.join(ir_workspace.get_path(), 'group_vars')
	if not os.path.exists(group_vars_file):
		os.makedirs(group_vars_file)
	for group in ir_workspace.get_groups():
		with open(os.path.join(group_vars_file, group), 'w') as f:
			pass

	# Set up the host_vars file
	host_vars_file = os.path.join(ir_workspace.get_path(), 'host_vars')
	if not os.path.exists(host_vars_file):
		os.makedirs(host_vars_file)
	for host in ir_workspace.get_hosts():
		with open(os.path.join(host_vars_file, host), 'w') as f:
			pass

	# Set up the roles directory
	roles_dir = os.path.join(ir_workspace.get_path(), 'roles')
	if not os.path.exists(roles_dir):
		os.makedirs(roles_dir)

	# Set up the plugins directory
	plugins_dir = os.path.join(ir_workspace.get_path(), 'plugins')
	if not os.path.exists(plugins_dir):
		os.makedirs(plugins_dir)

	# Set up the plugins directory
	plugins_dir = os.path.join(ir_workspace.get_path(), 'plugins')
	if not os.path.exists(plugins_dir):
		os.makedirs(plugins_dir)

	# Set up the