def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
	"""
	Together with :func:``update_last_applied_manifest_list_from_resp``, this
function is called recursively to update a partial ``last_applied_manifest``
from a partial Kubernetes response

Args:
    last_applied_manifest (dict): partial ``last_applied_manifest`` being
        updated
    observer_schema (dict): partial ``observer_schema``
    response (dict): partial response from the Kubernetes API.

Raises:
    KeyError: If the observed field is not present in the Kubernetes response

This function go through all observed fields, and initialized their value in
last_applied_manifest if they are not yet present
	"""
	for key, schema in observer_schema.items():
		if isinstance(schema, dict):
			update_last_applied_manifest_dict_from_resp(
				last_applied_manifest[key], schema, response)
		else:
			try:
				value = response['status']['conditions'][0]['status']
			except KeyError as e:
				raise KeyError("KeyError for %s" % str(e))
			last_applied_manifest[key] = value