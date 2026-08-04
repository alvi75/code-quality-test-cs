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
		verbose = ir_workspace.config.get('ansible', 'verbosity')
	if verbose is None:
		verbose = 0
	if verbose == 'debug':
		verbose = 4
	if verbose == 'info':
		verbose = 3
	if verbose == 'warning':
		verbose = 2
	if verbose == 'error':
		verbose = 1
	if verbose == 'quiet':
		verbose = 0
	if verbose is not None:
		verbose = int(verbose)
	if verbose < 0:
		verbose = 0
	if verbose > 4:
		verbose = 4
	if verbose == 0:
		verbose = None
	if verbose is not None:
		verbose = '-' + str(verbose)
	if extra_vars is None:
		extra_vars = {}
	if ansible_args is None:
		ansible_args = {}
	if 'extra-vars' in ansible_args:
		extra_vars.update(ansible_args['extra-vars'])
		del ansible_args['extra-vars']
	if 'ansible-args' in ansible_args:
		ansible_args.update(ansible_args['ansible-args'])
		del ansible_args['ans