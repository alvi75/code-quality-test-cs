def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not hasattr(_should_attempt_c_optimizations, "value"):
		import sys
		from distutils.sysconfig import get_config_var
		# XXX: This is a hack to work around a bug in setuptools 0.7 where
		#       it fails to find the correct version of gcc when using
		#       the C extensions.  We have to do this because the
		#       C extension will fail to build if the user has not
		#       installed gcc or if they have an old version of gcc.
		#
		#       The workaround is to set the environment variable
		#       CC=gcc-3.2.  This should be removed once the bug is fixed.
		if get_config_var("CC") == "gcc-3.2":
			sys.stderr.write("WARNING: Using GCC 3.2 for C extensions.\n")
			sys.stderr.write("        Please upgrade your GCC installation.\n")
		_should_attempt_c_optimizations.value = (get_config_var("OPTIMIZED") != "no")
	return _should_attempt_c_optimizations.value