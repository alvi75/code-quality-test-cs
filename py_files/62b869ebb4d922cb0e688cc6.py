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
	"""
	for i, field in enumerate(observer_schema):
		if isinstance(field, dict):
			update_last_applied_manifest_list_from_resp(
				last_applied_manifest[i],
				field,
				response[i]
			)
		else:
			if field not in last_applied_manifest[i]:
				last_applied_manifest[i][field] = response[i]