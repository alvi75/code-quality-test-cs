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
		raise ValueError("playbook_path must be specified")

	playbook_path = os.path.abspath(playbook_path)

	# If we have a workspace, use it to get the inventory file
	inventory_file = None
	if ir_workspace:
		inventory_file = ir_workspace.get_inventory_file()

	# If we have a plugin, use it to get the inventory file
	if not inventory_file and ir_plugin:
		inventory_file = ir_plugin.get_inventory_file()

	# If we still don't have an inventory file, use the default one
	if not inventory_file:
		inventory_file = os.path.join(os.getcwd(), "infrared", "inventory")

	# If we have a workspace, use it to get the inventory file
	if ir_workspace:
		inventory_file = ir_workspace.get_inventory_file()

	# If we have a plugin, use it to get the inventory file
	if not inventory_file and ir_plugin:
		inventory_file = ir_plugin.get_inventory_file()

	# If we still don't have an inventory file, use the default one
	if not inventory_file:
		inventory_file = os.path.join(os.getcwd(), "infrared", "inventory")

	# If we have a workspace, use it to get the inventory file
	if ir_workspace:
		inventory_file = ir_workspace.get_inventory_file()

	# If we have a plugin, use it to get the inventory file
	if not inventory_file and ir_plugin:
		inventory_file = ir_plugin.get_inventory_file()

	# If we still don't have an inventory file, use the default one
	if not inventory_file:
		inventory_file = os.path.join(os.getcwd(), "infrared", "inventory")

	# If we have a workspace, use it to get the inventory file
	if ir_workspace:
		inventory_file = ir_workspace.get_inventory_file()

	# If we have a plugin, use