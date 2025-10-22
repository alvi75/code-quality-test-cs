def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                    extra_vars=None, ansible_args=None):
	"""
	Wraps the 'ansible-playbook' CLI.

:param ir_workspace: An Infrared Workspace object represents the active
workspace
:param ir_plugin: An InfraredPlugin object of the current plugin
:param playbook_path: the playbook to invoke
:param verbose: Ansible verbosity level
:param extra_vars: dict. Passed to Ansible as extra-vars
:param ansible_args: dict of ansible-playbook arguments to plumb down
    directly to Ansible.
	"""
	if not playbook_path:
		raise ValueError('playbook_path is required')

	playbook_path = os.path.abspath(playbook_path)

	# If we have a workspace, use it to get the inventory file
	inventory_file = None
	if ir_workspace:
		inventory_file = ir_workspace.get_inventory_file()

	# If we have a plugin, use it to get the inventory file
	if ir_plugin:
		inventory_file = ir_plugin.get_inventory_file()

	# If we have a plugin, use it to get the inventory file
	if inventory_file:
		ansible_args['inventory'] = inventory_file

	# If we have a plugin, use it to get the inventory file
	if extra_vars:
		ansible_args['extra_vars'] = extra_vars

	# If we have a plugin, use it to get the inventory file
	if verbose:
		ansible_args['verbose'] = verbose

	# If we have a plugin, use it to get the inventory file
	if ansible_args:
		ansible_args.update({'ansible_args': ansible_args})

	# If we have a plugin, use it to get the inventory file
	if ir_plugin:
		ansible_args['plugin'] = ir_plugin.name

	# If we have a plugin, use it to get the inventory file
	if ir_workspace:
		ansible_args['workspace'] = ir_workspace.name

	# If we have a plugin, use it to get the inventory file
	if ir_workspace:
		ansible_args['workspace_dir'] = ir_workspace.workspace_dir

	# If we have a plugin, use it to get the inventory file
	if ir_workspace:
		ansible_args['workspace_config'] = ir_workspace.config

	# If we have a plugin, use it to get the inventory file
	if ir_workspace:
		ansible_args['workspace_inventory'] = ir_workspace.inventory

	# If we have a plugin, use