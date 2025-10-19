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

	# Create a new playbook directory if it doesn't exist already
	ir_workspace.playbooks[playbook_path] = Playbook(
			name=playbook_path,
			verbose=verbose,
			extra_vars=extra_vars)

	# Run the playbook
	try:
		shutit_global.shutit_global_object.shutit_print('Invoking playbook %s' % (playbook_path))
		# Use the default args for this call
		# TODO: This should be made more flexible by using the ansible module
		#       argument system
		# TODO: Make sure that we don't overwrite any existing playbook vars
		#       from previous playbooks
		# TODO: Allow user to override variables in the playbook with kwargs
		#       e.g., `ansible-playbook -o foo=bar`
		# TODO: Allow user to specify custom inventory file
		# TODO: Allow user to specify custom inventory source
		# TODO: Allow user to specify custom remote_user
		# TODO: Allow user to specify custom ssh options
		# TODO: Allow user to specify custom loglevel
		# TODO: Allow user to specify custom timeout
		# TODO: Allow user to specify custom sudo user
		# TODO: Allow user to specify custom sudo password
		# TODO: Allow user to specify custom sudo privs
		# TODO: Allow user to specify custom sudo command
		# TODO: Allow user to specify custom sudo chroot
		# TODO: Allow user to specify custom sudo capabilities
		# TODO: Allow user to specify custom sudo options
		# TODO: Allow user to specify custom sudo defaults
		# TODO: Allow user to specify custom sudo defaults
		# TODO