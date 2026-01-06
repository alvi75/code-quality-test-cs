def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
	"""
	Together with :func:``update_last_applied_manifest_dict_from_resp``, this
function is called recursively to update a partial ``last_applied_manifest``
from a partial Kubernetes response

Args:
    last_applied_manifest (list): partial ``last_applied_manifest`` being
        updated
    observer_schema (list): partial ``observer_schema``
    response (list): partial response from the Kubernetes API.

This function go through all observed fields, and initialized their value in
last_applied_manifest if they are not yet present
	"""
	for i, field in enumerate(observer_schema):
		if field['name'] == 'metadata':
			continue
		if field['name'] == 'status':
			continue
		if field['name'] == 'spec':
			continue
		if field['name'] == 'kind':
			continue
		if field['name'] == 'apiVersion':
			continue
		if field['name'] == 'type':
			continue
		if field['name'] == 'observedGeneration':
			continue
		if field['name'] == 'generation':
			continue
		if field['name'] == 'resourceVersion':
			continue
		if field['name'] == 'uid':
			continue
		if field['name'] == 'selfLink':
			continue
		if field['name'] == 'creationTimestamp':
			continue
		if field['name'] == 'annotations':
			continue
		if field['name'] == 'deletionTimestamp':
			continue
		if field['name'] == 'deletionGracePeriodSeconds':
			continue
		if field['name'] == 'finalizers':
			continue
		if field['name'] == 'ownerReferences':
			continue
		if field['name'] == 'initializers':
			continue
		if field['name'] == 'managedFields':
			continue
		if field['name'] == 'clusterName':
			continue
		if field['name'] == 'namespace':
			continue
		if field['name'] == 'name':
			continue
		if field['name'] == 'kind':
			continue
		if field['name'] == 'apiVersion':
			continue
		if field['name'] == 'type':
			continue
		if field['name'] == 'observedGeneration':
			continue
		if field['name'] == 'generation':