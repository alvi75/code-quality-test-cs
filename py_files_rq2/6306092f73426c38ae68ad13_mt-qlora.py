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

	# TODO: This should be a configuration option
	ansible_args = ansible_args or {}

	# TODO: This should be a configuration option
	extra_vars = extra_vars or {}

	# TODO: This should be a configuration option
	verbosity = verbose or 0

	# TODO: This should be a configuration option
	env = os.environ.copy()

	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This should be a configuration option
	# TODO: This