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
	for i, item in enumerate(observer_schema):
		if isinstance(item, dict):
			if "path" not in item.keys():
				raise ValueError("dict without path key")
			if item["path"] == "":
				item["path"] = [i]
			elif not isinstance(item["path"], list):
				item["path"] = [item["path"]]
			update_last_applied_manifest_list_from_resp(
				last_applied_manifest,
				item["path"],
				response[item["path"][0]],
			)
		else:
			if (
				item not in last_applied_manifest[i]
				and item != ""
			):  # "" should be considered as None
				last_applied_manifest[i][item] = ""

	return last_applied_manifest