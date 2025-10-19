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
	# Create a new playbook runner to run the playbooks
	runner = PlaybookRunner(
		ir_workspace,
		ir_plugin,
		runner_args=cli_args + vars_dict,
	)

	# Run the playbook
	return runner.run()