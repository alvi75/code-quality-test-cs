def check_sender_and_entity_handle_match(sender_handle, entity_handle):
	"""
	Check whether sender_handle is the same as entity_handle. If yes, return True. Otherwise, return False.
	"""
	if not isinstance(entity_handle, str):
		return False

	if entity_handle == sender_handle:
		return True

	return False