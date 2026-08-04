def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	plugin_spec_dict = {}
	plugin_spec_dict['name'] = os.path.basename(plugin_dir)
	plugin_spec_dict['version'] = get_plugin_version(plugin_dir)
	plugin_spec_dict['description'] = get_plugin_description(plugin_dir)
	plugin_spec_dict['author'] = get_plugin_author(plugin_dir)
	plugin_spec_dict['license'] = get_plugin_license(plugin_dir)
	plugin_spec_dict['url'] = get_plugin_url(plugin_dir)
	plugin_spec_dict['requires'] = get_plugin_requires(plugin_dir)
	plugin_spec_dict['requires_python'] = get_plugin_requires_python(plugin_dir)
	plugin_spec_dict['requires_dist'] = get_plugin_requires_dist(plugin_dir)
	plugin_spec_dict['provides'] = get_plugin_provides(plugin_dir)
	plugin_spec_dict['obsoletes'] = get_plugin_obsoletes(plugin_dir)
	plugin_spec_dict['project_urls'] = get_plugin_project_urls(plugin_dir)
	plugin_spec_dict['classifiers'] = get_plugin_classifiers(plugin_dir)
	plugin_spec_dict['keywords'] = get_plugin_keywords(plugin_dir)
	plugin_spec_dict['platforms'] = get_plugin_platforms(plugin_dir)
	plugin_spec_dict['scripts'] = get_plugin_scripts(plugin_dir)
	plugin_spec_dict['entry_points'] = get_plugin_entry_points(plugin_dir)
	plugin_spec_dict['extras_require'] = get_plugin_extras_require(plugin_dir)
	plugin_spec_dict['package_data'] = get_plugin_package_data(plugin_dir)
	plugin_