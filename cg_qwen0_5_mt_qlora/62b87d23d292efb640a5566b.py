def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		commands = [commands]
	if not isinstance(args, (list, tuple)):
		args = [args]

	# set up the environment
	env = env or os.environ

	# get the command to run
	command = commands[0] if len(commands) == 1 else commands

	# get the arguments to pass to the command
	arguments = args[0] if len(args) == 1 else args

	# get the working directory
	cwd = cwd or os.getcwd()

	# get the verbosity level
	verbosity = int(verbosity)

	# get the output format
	output_format = 'text' if not hide_stderr else 'json'

	# get the logging level
	log_level = logging.DEBUG if verbosity > 2 else logging.INFO

	# create a logger
	logger = logging.getLogger('subprocess')
	logger.setLevel(log_level)

	# create a formatter
	fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# add the formatter to the logger
	logger.addHandler(logging.StreamHandler())

	# add the handler to the logger
	logger.addHandler(logging.FileHandler(os.path.join(cwd, 'subprocess.log')))

	# create a sub-process
	p = subprocess.Popen(command,
		shell=True,
		cwd=cwd,
		verbose=not verbose,
		creationflags=0,
		kwargs={'stdout': subprocess.PIPE,
				'stderr': subprocess.STDOUT},
		env=env)

	# read the output from the process
	out, err = p.communicate()

	# check the exit status of the process
	if p.returncode != 0:
		# print the error message
		if not hide_stderr:
			sys.stderr.write(err.decode('utf-8'))

		# raise an exception
		raise SubprocessError(p.returncode, out, err)

	# return the output
	return out.decode('utf-8')