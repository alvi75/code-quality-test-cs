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
	# TODO: add support for other types of plugins
	if not ir_workspace:
		raise ValueError("Workspace is None")
	if not ir_plugin:
		raise ValueError("Plugin is None")

	# Get the inventory
	inventory = ir_workspace.get_inventory()
	if not inventory:
		raise ValueError("Inventory is None")

	# Get the playbook
	playbook = ir_plugin.get_playbook(playbook_path)

	# Get the vars
	vars = {}
	if extra_vars:
		for k, v in extra_vars.items():
			vars[k] = v

	# Get the args
	args = {}
	if ansible_args:
		for k, v in ansible_args.items():
			args[k] = v

	# Run the playbook
	try:
		ansible.run_playbook(
			inventory=inventory,
			playbook=playbook,
			vars=vars,
			args=args,
			verbose=verbose)
	except Exception as e:
		raise AnsibleError(e)