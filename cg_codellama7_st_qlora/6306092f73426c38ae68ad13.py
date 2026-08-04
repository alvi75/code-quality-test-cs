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
		verbose = ir_workspace.verbose

	if extra_vars is None:
		extra_vars = {}

	if ansible_args is None:
		ansible_args = {}

	# Set the default verbosity level
	if verbose:
		ansible_args['verbosity'] = verbose

	# Set the default inventory
	if 'inventory' not in ansible_args:
		ansible_args['inventory'] = ir_workspace.inventory_path

	# Set the default playbook
	if 'playbook' not in ansible_args:
		ansible_args['playbook'] = playbook_path

	# Set the default extra-vars
	if 'extra-vars' not in ansible_args:
		ansible_args['extra-vars'] = extra_vars

	# Set the default ansible-playbook arguments
	if 'ansible-playbook' not in ansible_args:
		ansible_args['ansible-playbook'] = []

	# Set the default ansible-playbook arguments
	if 'ansible-playbook' not in ansible_args:
		ansible_args['ansible-playbook'] = []

	# Set the default ansible-playbook arguments
	if 'ansible-playbook' not in ansible_args:
		ansible_