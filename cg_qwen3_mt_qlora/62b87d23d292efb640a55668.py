def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if not os.path.exists(config.vcext_module):
		raise VersionControlError(
			"Can't find vcversioner module: %s" % config.vcext_module)
	try:
		execfile(config.vcext_module, {}, config.__dict__)
	except IOError as e:
		raise VersionControlError("Can't read vcversioner module: %s" % e)
	except Exception as e:
		raise VersionControlError("Error in vcversioner module: %s" % e)

	if not hasattr(config, 'get_vcs_version'):
		raise VersionControlError(
			"vcversioner module doesn't have get_vcs_version function")
	return config