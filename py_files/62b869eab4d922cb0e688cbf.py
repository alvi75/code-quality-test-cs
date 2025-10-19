def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for k8s_type, k8s_obj in app.spec.manifest.items():
		if not isinstance(k8s_obj, dict) or 'kind' not in k8s_obj:
			continue

		k8s_type = k8s_type.lower()
		if k8s_type == 'api':
			yield k8s_type, KubeApiSchema
		elif k8s_type == 'customresource':
			yield k8s_type, KubeCustomResourceSchema
		else:
			yield k8s_type, KubeObjectSchema