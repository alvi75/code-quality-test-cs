def subprocess_run_helper(func, *args, timeout, extra_env=None):
	"""
	Run a function in a sub-process

    Args:
            func: function, the function to be run. It must be in a module that is importable.
            *args: str. Any additional command line arguments to be passed in
                        the first argument to ``subprocess.run``.
            extra_env: dict[str, str]. Any additional environment variables to be set for the subprocess.
    Returns:
            CompletedProcess instance
	"""
	import inspect
	import os
	import shutil
	import signal
	import subprocess
	import sys
	import tempfile
	import time
	import traceback
	import types
	import uuid

	def get_func_source(func):
		"""
		Get source code of a function as string.

		Args:
			func (function): Function whose source code we want.

		Returns:
			str: Source code of the function.
		"""

		if isinstance(func, types.MethodType):
			func = func.__func__

		if not isinstance(func, types.FunctionType):
			raise TypeError("Expected function type.")

		file_name = func.__code__.co_filename
		function_name = func.__code__.co_name

		with open(file_name) as f:
			source_code = f.readlines()

		source_lines, _ = inspect.getsourcelines(func)
		source_code.extend(source_lines)

		start_line_no = func.__code__.co_firstlineno - 1
		end_line_no = start_line_no + len(source_lines)

		return "".join(source_code[start_line_no:end_line_no])

	def write_temp_file(source_code):
		temp_dir = tempfile.gettempdir()
		temp_file_name = os.path.join(temp_dir, "tmp_%s.py" % str(uuid.uuid4()))

		with open(temp_file_name, "w") as f:
			f.write(source_code)

		return temp_file_name

	def execute_command(command, env):
		"""
		Execute a command in a sub-process

		Args:
			command (list(str)): The command to be executed.
			env (dict[str, str]): Environment variables to be set before execution.
		Returns:
			subprocess.CompletedProcess: The completed process instance.
		"""

		process = subprocess.run(
			command,
			timeout=timeout,
			check=True,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			encoding="utf-8",
			shell=False,
			env=env,
		)

		return process