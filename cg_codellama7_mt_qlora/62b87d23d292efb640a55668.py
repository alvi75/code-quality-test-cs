def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = os.environ.get('Versioneer_VCS', 'git')
	config.VCS_PREFIXES = os.environ.get('Versioneer_VCS_PREFIXES', '(tag: )(branch: )(revision: )(commit: )').split()
	config.VCS_METADATA = os.environ.get('Versioneer_VCS_METADATA', '').split()
	config.VCS_METADATA_PREFIX = os.environ.get('Versioneer_VCS_METADATA_PREFIX', '(')
	config.VCS_METADATA_SUFFIX = os.environ.get('Versioneer_VCS_METADATA_SUFFIX', ')')
	config.VCS_METADATA_VERSION = os.environ.get('Versioneer_VCS_METADATA_VERSION', 'version')
	config.VCS_METADATA_VERSION_PREFIX = os.environ.get('Versioneer_VCS_METADATA_VERSION_PREFIX', '(')
	config.VCS_METADATA_VERSION_SUFFIX = os.environ.get('Versioneer_VCS_METADATA_VERSION_SUFFIX', ')')
	config.VCS_METADATA_VERSION_PATTERN = os.environ.get('Versioneer_VCS_METADATA_VERSION_PATTERN', '(?P<version>[^)]+)')
	config.VCS_METADATA_VERSION_REGEX = re.compile(config.VCS_METADATA_VERSION_PATTERN)
	config.VCS_METADATA_VERSION_REGEX_GROUP = config.VCS_METADATA_VERSION_REGEX.groupindex[config.VCS_METADATA_VERSION]
	config.VCS_METADATA