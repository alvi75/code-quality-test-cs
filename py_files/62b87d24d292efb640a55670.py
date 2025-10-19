def get_versions():
		""" Obtains the version information. If the version information cannot be obtained, the default value is returned. """
		try:
			return __version_info__
		except Exception as e:
			print("Error: " + str(e))
			return ("0.0.0", 0)