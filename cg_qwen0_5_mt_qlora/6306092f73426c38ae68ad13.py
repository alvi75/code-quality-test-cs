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
	if not os.path.exists(playbook_path):
		raise IOError("Playbook does not exist at %s" % playbook_path)

	# Get the inventory from the workspace
	inventory = ir_workspace.get_inventory()

	# Get the playbook from the workspace
	playbook = ir_workspace.get_playbook(playbook_path)

	# Get the playbook vars from the workspace
	playbook_vars = ir_workspace.get_playbook_vars(playbook_path)

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir_plugin.get_playbook_vars(playbook_path))

	# Get the playbook vars from the workspace
	playbook_vars.update(ir