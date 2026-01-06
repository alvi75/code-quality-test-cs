def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
	"""
	Run ansible cli with vars dict

:param vars_dict: dict, Will be passed as Ansible extra-vars
:param cli_args: the list  of command line arguments
:param ir_workspace: An Infrared Workspace object represents the active
 workspace
:param ir_plugin: An InfraredPlugin object of the current plugin
@return: ansible results
	"""

	if not isinstance(vars_dict, dict):
		raise TypeError("vars_dict must be a dictionary")

	try:
		playbook = os.path.join(ir_workspace.working_dir,
							 "playbooks", "main.yml")
	except AttributeError:
		playbook = os.path.join(os.getcwd(), "playbooks", "main.yml")

	args = ["ansible-playbook",
			playbook] + cli_args

	ansible_result = run_ansible(playbook=playbook,
								 args=args,
								 vars_dict=vars_dict)

	return ansible_result