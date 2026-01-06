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
	for field in last_applied_manifest:
		if field == 'observedBy':
			last_applied_manifest[field] = response[0][field]
		elif field == 'lastAppliedManifest':
			last_applied_manifest[field] = response[1][field]
		else:
			for schema in observer_schema:
				if field == schema['name']:
					field_value = response[0][schema['path']]
					if field_value != None:
						last_applied_manifest[field] = field_value
					break
	return last_applied_manifest