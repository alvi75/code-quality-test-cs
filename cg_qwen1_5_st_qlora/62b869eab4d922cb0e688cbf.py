def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for k8s_resource, manifest in app.spec.manifest.items():
		if not hasattr(manifest, 'schema'):
			continue

		resource = kubernetes.client.V1ObjectReference(
			api_version=manifest.apiVersion,
			group=manifest.group,
			version=manifest.version,
			name=manifest.name,
			namespace=manifest.namespace,
			resource=kubernetes.client.ObjectMeta(name=manifest.name)
		)

		app.schema[k8s_resource] = {
			'apiVersion': 'kubeflow.org/v1',
			'description': 'Default schema for {} resources'.format(k8s_resource),
			'schema': {
				'$ref': '#/components/schemas/' + k8s_resource
			}
		}