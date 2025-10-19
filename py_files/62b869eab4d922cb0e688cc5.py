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
"""

	for k, v in list(last_applied_manifest.items()):
		if k not in observer_schema:
			raise KeyError("The observed field '{}' was not found in the "
			   "Kubernetes response".format(k))

		last_applied_manifest[k] = v

	return last_applied_manifest