def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	global _config
	if not _config:
		_config = VersioneerConfig()
		_config._version = 0
		_config._release = 0
		_config._tag = None
		_config._commit = None
		_config._branch = None
		_config._git_dir = None
		_config._git_hash = None
		_config._git_tag = None
		_config._git_commit = None
		_config._git_branch = None
		_config._git_repo = None
		_config._git_url = None
		_config._git_user = None
		_config._git_email = None
		_config._git_remote = None
		_config._git_remote_url = None
		_config._git_remote_username = None
		_config._git_remote_password = None
		_config._git_remote_ssh_key = None
		_config._git_remote_ssh_key_path = None
		_config._git_remote_ssh_key_file = None
		_config._git_remote_ssh_key_type = None
		_config._git_remote_ssh_key_format = None
		_config._git_remote_ssh_key_format_path = None
		_config._git_remote_ssh_key_format_file = None
		_config._git_remote_ssh_key_format_type = None
		_config._git_remote_ssh_key_format_type_path = None
		_config._git_remote_ssh_key_format_type_file = None
		_config._git_remote_ssh_key_format_type_format = None
		_config._git_remote_ssh_key_format_type_format_path = None
		_config._git_remote_ssh_key_format_type_format_file = None
		_config._git_remote_ssh_key_format_type_format_type = None
		_config._git_remote_ssh_key_format_type_format_type_path = None
		_config._git_remote_ssh_key_format_type_format_type_file = None
		_config._git_remote_ssh_key_format_type_format_type_format = None
		_config._git_remote_ssh_key_format_type_format_type_format_path = None
		_config._git_remote_ssh_key_format_type_format_type_format_file = None
		_config._git_remote_ssh_key_format_type_format_type_format_type = None
		_config._git_remote_ssh_key_format_type_format_type_format_type_path = None
		_config._git_remote_ssh_key_format