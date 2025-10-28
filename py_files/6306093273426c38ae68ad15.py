def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
	"""
	Runs ansible cli with vars dict

:param vars_dict: dict, Will be passed as Ansible extra-vars
:param cli_args: the list  of command line arguments
:param ir_workspace: An Infrared Workspace object represents the active
 workspace
:param ir_plugin: An InfraredPlugin object of the current plugin
:return: ansible results
	"""
	if not isinstance(vars_dict, dict):
		raise TypeError("vars_dict must be a dictionary")

	playbook = os.path.join(ir_workspace.get_path(), 'playbooks', 'main.yml')
	ansible_cmd = ['ansible-playbook']
	ansible_cmd.extend(['-i', 'localhost,', '127.0.0.1'])
	ansible_cmd.extend(['--extra-vars', json.dumps(vars_dict)])
	ansible_cmd.append(playbook)
	return subprocess.check_output(ansible_cmd)