def get_plugin_spec_flatten_dict(plugin_dir):
	"""
	Use YAML to read various information in plugin_dir and return the information in dictionary form.
	"""
	spec = {}
	for filename in os.listdir(plugin_dir):
		if not filename.endswith('.yaml'):
			continue

		file_path = os.path.join(plugin_dir, filename)
		with open(file_path) as f:
			data = yaml.load(f)

		name = data['name']
		version = data.get('version', '0.1')
		description = data.get('description', '')
		slug = name.lower().replace(' ', '-')

		spec[slug] = {
			'name': name,
			'version': version,
			'description': description,
			'file_name': filename,
			'slug': slug,
			'path': file_path,
			'registry_url': data.get('registry_url'),
			'metadata': data.get('metadata'),
			'config_schema': data.get('config_schema'),
			'api_version': data.get('api_version'),
			'plugin_type': data.get('plugin_type'),
			'category': data.get('category'),
			'author': data.get('author'),
			'license': data.get('license'),
			'keywords': data.get('keywords'),
			'homepage': data.get('homepage'),
			'issues_url': data.get('issues_url'),
			'test_suite_url': data.get('test_suite_url'),
			'github_repo_url': data.get('github_repo_url'),
			'gitlab_repo_url': data.get('gitlab_repo_url'),
			'homedir': data.get('homedir'),
			'install_script': data.get('install_script'),
			'uninstall_script': data.get('uninstall_script'),
			'build_script': data.get('build_script'),
			'run_script': data.get('run_script'),
			'package_script': data.get('package_script'),
			'upload_script': data.get('upload_script'),
			'update_script': data.get('update_script'),
			'pre_install_script': data.get('pre_install_script'),
			'post_install_script': data.get('post_install_script'),
			'pre_uninstall_script': data.get('pre_uninstall_script'),
			'post_uninstall_script': data.get('post_uninstall_script'),
			'pre_build_script': data.get('pre_build_script'),
			'post_build