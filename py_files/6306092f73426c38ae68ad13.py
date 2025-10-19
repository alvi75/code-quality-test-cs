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
		raise ValueError("Playbook does not exist: %s" % (playbook_path))

	# TODO: support for extra-vars

	# TODO: support for private_data_dir

	# TODO: support for inventory

	# TODO: support for callbacks

	# TODO: support for forks

	# TODO: support for sudo

	# TODO: support for sudo_user

	# TODO: support for transport

	# TODO: support for module_path

	# TODO: support for forks

	# TODO: support for remote_user

	# TODO: support for remote_pass

	# TODO: support for check

	# TODO: support for become

	# TODO: support for become_user

	# TODO: support for become_pass

	# TODO: support for async

	# TODO: support for poll

	# TODO: support for timeout

	# TODO: support for on_error_continue

	# TODO: support for private_key_file

	# TODO: support for private_key

	# TODO: support for ssh_common_args

	# TODO: support for ssh_pass

	# TODO: support for venv

	# TODO: support for tags

	# TODO: support for skip_tags

	# TODO: support for extra_tags

	# TODO: support for on_success_continue

	# TODO: support for on_failure_continue

	# TODO: support for on_failure_abort

	# TODO: support for on_success_abort

	# TODO: support for private_key_file

	# TODO: support for private_key

	# TODO: support for ssh_common_args

	# TODO: support for ssh_pass

	# TODO: support for on_error_continue

	# TODO: support for on_success_continue

	# TODO: support for on_failure_continue

	# TODO: support for on_failure_abort