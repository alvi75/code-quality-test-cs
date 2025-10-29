def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not hasattr(_should_attempt_c_optimizations, "_cached"):
		# We don't know whether to use C optimizations yet, so cache this result
		# for future use.
		#
		# Note that this is a bit of a hack - it's possible that the compiler
		# will be able to optimize away some of our functions in the future,
		# but we still want to try to avoid using C optimizations just in case.
		#
		# If we're going to use C optimizations, then we'll need to set
		# `_should_attempt_c_optimizations._cached` to `True`.
		#
		# If we're not going to use C optimizations, then we'll need to set
		# `_should_attempt_c_optimizations._cached` to `False`.
		#
		# This is a bit of a hack, but it should work for most cases.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a command line flag.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a command line flag.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		# TODO: Consider making this configurable via a config file or similar.
		#
		#