def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.versionfile_source = versionfile_source
	config.versionfile_template = versionfile_template
	config.versionfile_format = versionfile_format
	config.build_command = build_command
	config.build_args = build_args
	config.finalize_on_commit = finalize_on_commit
	config.finalize_after_build = finalize_after_build
	config.tag_prefix = tag_prefix
	config.versionfile_is_executable = versionfile_is_executable
	config.versionfile_is_module = versionfile_is_module
	return config