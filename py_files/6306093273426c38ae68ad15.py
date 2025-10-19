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
	# TODO: Add support for other platforms than Linux/OSX
	if platform.system() == 'Linux' or platform.system() == 'Darwin':
		# TODO: Make this configurable
		runner = subprocess.Popen(
			['ansible-playbook', '--become', '-i',
				'/home/{0}/.ansible/tmp/hosts'.format(getpass.getuser()),
				'-e', json.dumps(vars_dict), cli_args],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
	else:
		raise NotImplementedError()
	return runner