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
		raise ValueError("playbook_path is required")

	# TODO: add support for --inventory-file
	# TODO: add support for --list-hosts

	# TODO: add support for --check
	# TODO: add support for --diff
	# TODO: add support for --syntax-check

	# TODO: add support for --tags
	# TODO: add support for --skip-tags

	# TODO: add support for --limit

	# TODO: add support for --private-key
	# TODO: add support for --ssh-common-args
	# TODO: add support for --become-method
	# TODO: add support for --become-user
	# TODO: add support for --become-method
	# TODO: add support for --become-user
	# TODO: add support for --ask-become-pass
	# TODO: add support for --ask-sudo-pass

	# TODO: add support for --extra-vars
	# TODO: add support for --extra-vars-file

	# TODO: add support for --forks
	# TODO: add support for --forks-file

	# TODO: add support for --module-path
	# TODO: add support for --module-path-file

	# TODO: add support for --private-key-file
	# TODO: add support for --ssh-common-args-file

	# TODO: add support for --sudo
	# TODO: add support for --sudo-user
	# TODO: add support for --ask-sudo-pass

	# TODO: add support for --vault-password-file

	# TODO: add support for --connection
	# TODO: add support for --ssh-common-args
	# TODO: add support for --ssh-extra-args
	# TODO: add support for --ssh-pkey
	# TODO: