def update_last_applied_manifest_from_resp(last_applied_manifest, observer_schema, response):
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
	for k, v in observer_schema.items():
		if isinstance(v, dict) and "field" in v:
			last_applied_manifest[k] = response[v["field"]]
		elif isinstance(v, list) and "fields" in v:
			update_last_applied_manifest_list_from_resp(last_applied_manifest[k], v, response)
		else:
			raise KeyError("Kubernetes response does not contain {}".format(k))