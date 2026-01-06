def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.vcs = get_vcs_name()
	config.versionfile_source = get_versionfile_source()
	config.versionfile_build = get_versionfile_build()
	config.tag_prefix = get_tag_prefix()
	config.parentdir_prefix = get_parentdir_prefix()
	config.commit_msg_cleanup = get_commit_msg_cleanup()
	config.dont_edit_setup_py = get_dont_edit_setup_py()
	config.vcs_excludes = get_vcs_excludes()
	return config