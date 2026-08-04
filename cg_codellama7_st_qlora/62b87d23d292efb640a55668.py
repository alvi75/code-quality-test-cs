def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.VCS = os.environ.get('VersioneerVCS', 'git')
	config.VCS_PYPI = os.environ.get('VersioneerVCSPyPI', 'git')
	config.VCS_PYPI_URL = os.environ.get('VersioneerVCSPyPIURL', 'git')
	config.VCS_PYPI_URL_SCHEME = os.environ.get('VersioneerVCSPyPIURLScheme', 'git')
	config.VCS_PYPI_URL_PATH = os.environ.get('VersioneerVCSPyPIURLPath', 'git')
	config.VCS_PYPI_URL_QUERY = os.environ.get('VersioneerVCSPyPIURLQuery', 'git')
	config.VCS_PYPI_URL_FRAGMENT = os.environ.get('VersioneerVCSPyPIURLFragment', 'git')
	config.VCS_PYPI_URL_USER = os.environ.get('VersioneerVCSPyPIURLUser', 'git')
	config.VCS_PYPI_URL_PASSWORD = os.environ.get('VersioneerVCSPyPIURLPassword', 'git')
	config.VCS_PYPI_URL_HOST = os.environ.get('VersioneerVCSPyPIURLHost', 'git')
	config.VCS_PYPI_URL_PORT = os.environ.get('VersioneerVCSPyPIURLPort', 'git')
	config.VCS_PYPI_URL_PATH_SCHEME = os.environ.get('VersioneerVCSPyPIURLPathScheme', 'git')
	config.VCS_PYPI_URL_PATH_USER = os.environ.get('VersioneerVCSPyPIURLPathUser', 'git')
	config.VCS_PYPI_URL_PATH_PASSWORD = os.environ.get('VersioneerVCSPyPIURL