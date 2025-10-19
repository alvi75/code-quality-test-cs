def get_versions():
		"""
		Obtains the version information. If the version information cannot be obtained, the default value is returned.
		"""
		if not hasattr(get_versions, "version"):
			get_versions.version = None

		return get_versions.version

	get_versions.version = __get_version()
	return get_versions.version