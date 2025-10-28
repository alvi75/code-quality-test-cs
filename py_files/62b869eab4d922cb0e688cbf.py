def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for manifest in app.spec.manifest:
		if not manifest.get('observerSchema'):
			manifest['observerSchema'] = {
				'properties': {
					'name': {'type': 'string'},
					'spec': {'$ref': '#/definitions/' + manifest['kind'].lower() + 'Spec'}
				},
				'required': ['name', 'spec']
			}