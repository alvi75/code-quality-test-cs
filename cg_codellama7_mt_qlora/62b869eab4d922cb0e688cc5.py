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
	for field_name, field_schema in observer_schema.items():
		if field_name in response:
			if isinstance(field_schema, dict):
				if field_name not in last_applied_manifest:
					last_applied_manifest[field_name] = {}
				update_last_applied_manifest_dict_from_resp(
					last_applied_manifest[field_name],
					field_schema,
					response[field_name],
				)
			elif isinstance(field_schema, list):
				if field_name not in last_applied_manifest:
					last_applied_manifest[field_name] = []
				update_last_applied_manifest_list_from_resp(
					last_applied_manifest[field_name],
					field_schema,
					response[field_name],
				)
			else:
				last_applied_manifest[field_name] = response[field_name]