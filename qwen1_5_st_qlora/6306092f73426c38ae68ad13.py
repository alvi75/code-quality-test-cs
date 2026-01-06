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
		raise Exception("Playbook does not exist at %s" % playbook_path)

	playbook_dir = os.path.dirname(playbook_path)
	playbook_name = os.path.basename(playbook_path)

	# Get the path to the executable
	# TODO: This is a hack until we have a better way to get this information
	# from the plugin
	plugin_path = os.path.join(os.getcwd(), "infrared")
	exe_path = os.path.join(plugin_path, "bin", "ansible-playbook")

	# Set up the environment variables for Ansible
	env = os.environ.copy()
	env["ANSIBLE_CONFIG"] = os.path.join(plugin_path, "etc", "ansible.cfg")
	env["ANSIBLE_ROLES_PATH"] = os.path.join(plugin_path, "roles")
	env["ANSIBLE_INVENTORY_PATH"] = os.path.join(playbook_dir, "inventory.ini")
	env["INFRARED_WORKSPACE_DIR"] = os.path.abspath(ir_workspace.workspace_dir)
	env["INFRARED_PLUGIN_NAME"] = ir_plugin.name

	# Add any extra vars passed in
	if extra_vars:
		for key, value in six.iteritems(extra_vars):
			env[key] = value

	# Add any additional args passed in
	if ansible_args:
		for key, value in six.iteritems(ansible_args):
			env[key] = value

	# Run the command
	cmd = [exe_path]
	cmd.extend(["-i", playbook_dir])
	cmd.append(playbook_name)
	return subprocess.call(cmd, env=env)