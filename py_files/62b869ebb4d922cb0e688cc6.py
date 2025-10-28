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
	for field_name, field_value in zip(observer_schema, response):
		if isinstance(field_value, list) and len(last_applied_manifest) == 0:
			last_applied_manifest.append([])
		elif isinstance(field_value, dict) and len(last_applied_manifest) == 0:
			last_applied_manifest.append({})
		elif field_name not in last_applied_manifest:
			last_applied_manifest[field_name] = field_value