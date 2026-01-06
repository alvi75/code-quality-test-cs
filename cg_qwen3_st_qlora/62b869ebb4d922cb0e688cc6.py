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
		if isinstance(field, dict):
			# If the field is a dictionary, it means that we have to recurse
			# into it
			update_last_applied_manifest_list_from_resp(
				last_applied_manifest[i],
				field,
				response[field["name"]],
			)
		else:
			# If the field is not a dictionary, it means that we can just set
			# its value
			last_applied_manifest[i] = response[field]["value"]