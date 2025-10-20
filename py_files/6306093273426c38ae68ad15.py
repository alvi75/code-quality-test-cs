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
		raise ValueError("vars_dict must be a dictionary")

	playbook = os.path.join(ir_workspace.working_dir,
							 "playbooks", "main.yml")
	ansible_cmd = ["ansible-playbook",
					"-i", os.path.join(ir_workspace.working_dir, "hosts"),
					"-e", json.dumps(vars_dict),
					playbook]

	ansible_result = subprocess.run(ansible_cmd, stdout=subprocess.PIPE)

	return ansible_result.stdout.decode()