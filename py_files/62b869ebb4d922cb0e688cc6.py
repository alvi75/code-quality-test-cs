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

	for field_name, field_schema in zip(observer_schema, last_applied_manifest):

		if 'type' in field_schema:

			if 'items' in field_schema['type']:

				if isinstance(response, list) or isinstance(response, dict):

					update_last_applied_manifest_list_from_resp(last_applied_manifest, field_schema, response)

			else:

				if isinstance(field_schema, str):

					if field_name == 'timestamp':

						last_applied_manifest.append({'name': field_name,
						                           'value': time.time()})

					else:

						raise InvalidObserverSchemaException('Invalid schema for '
						                                 'field {}'.format(field_name))

				else:

					raise InvalidObserverSchemaException('Invalid schema for '
						                                 'field {}'.format(field_name))

		elif 'items' in field_schema:

			if isinstance(response, list) or isinstance(response, dict):

				update_last_applied_manifest_list_from_resp(last_applied_manifest, field_schema, response)

			else:

				raise InvalidObserverSchemaException('Invalid schema for '
						                                 'field {}'.format(field_name))