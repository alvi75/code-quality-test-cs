def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for kubernetes_resource in app.spec.manifest:
		if not isinstance(kubernetes_resource, dict) or 'schema' not in kubernetes_resource:
			continue

		kubernetes_resource['schema'] = generate_default_observer_schema_for_kubernetes_resource(kubernetes_resource)
		yield kubernetes_resource