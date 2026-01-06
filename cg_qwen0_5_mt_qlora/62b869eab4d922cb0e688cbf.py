def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for kubernetes_resource in app.spec.manifest:
		if 'customObserverSchema' not in kubernetes_resource:
			continue

		kubernetes_resource['schema'] = generate_custom_observer_schema(kubernetes_resource)