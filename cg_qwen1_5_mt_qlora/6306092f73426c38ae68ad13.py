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
		raise IOError("Playbook '%s' does not exist" % playbook_path)

	playbook = os.path.abspath(playbook_path)
	ansible_args = ansible_args or {}
	ansible_args.setdefault('extra_vars', extra_vars)
	ansible_args.setdefault('verbose', verbose)
	ansible_args.setdefault('inventory', ir_workspace.inventory_path)
	ansible_args.setdefault('tags', None)  # TODO: tags

	args = ['ansible-playbook']
	args.extend([str(x) for x in ansible_args])
	args.append(playbook)

	return subprocess.call(args)