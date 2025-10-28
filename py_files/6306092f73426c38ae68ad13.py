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
		raise IOError("Playbook %s does not exist" % playbook_path)

	playbook = os.path.abspath(playbook_path)
	args = ['--inventory', ir_plugin.inventory_file]
	if verbose:
		args.append('-v')
	else:
		args.append('--quiet')

	if extra_vars is None:
		extra_vars = {}
	for key in sorted(extra_vars.keys()):
		args.extend(['-e', '%s=%s' % (key, extra_vars[key])])

	if ansible_args is None:
		ansible_args = {}

	# Add any additional args that were passed in
	args.extend(ansible_args['args'])

	# Now add the playbook path
	args.append(playbook)

	# Run the command
	return subprocess.call(args)