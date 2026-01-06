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
	if verbose is None:
		verbose = ir_plugin.verbose

	if ansible_args is None:
		ansible_args = {}

	# If we have a playbook path, then we need to set the playbook
	# directory in the ansible args
	if playbook_path:
		ansible_args['--playbook-directory'] = os.path.dirname(playbook_path)

	# If we have extra vars, then we need to set them in the ansible args
	if extra_vars:
		ansible_args['--extra-vars'] = extra_vars

	# If we have verbose, then we need to set it in the ansible args
	if verbose:
		ansible_args['--verbose'] = str(verbose)

	# If we have ansible_args, then we need to merge them with the ansible
	# args
	if ansible_args:
		ansible_args.update(ansible_args)

	# Now we can run ansible-playbook
	shell_command = ['ansible-playbook', '-i', ir_workspace.workspace_id,
					 '-e', 'ansible_python_interpreter=/usr/bin/python',
					 '-e', 'ansible_python_interpreter=python2.7',
					 '-e', 'ansible_python_interpreter=python3.4',
					 '-e', 'ansible_python_interpreter=python2.6',
					 '-e', 'ansible_python_interpreter=python2.5',
					 '-e', 'ansible_python_interpreter=python2.4',
					 '-e', 'ansible_python_interpreter=python2.3',
					 '-e', 'ansible_python_interpreter=python2.0',
					 '-e', 'ansible_python_interpreter=python1.8',
					 '-e', 'ansible_python_interpreter=python1.9',
					 '-e', 'ansible_python_interpreter=python1.10',
					 '-e', 'ansible_python_interpreter=python1.11',
					 '-e', 'ansible_python