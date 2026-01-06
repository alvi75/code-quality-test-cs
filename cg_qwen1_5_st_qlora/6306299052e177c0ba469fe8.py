def check_sender_and_entity_handle_match(sender_handle, entity_handle):
	"""
	Check whether sender_handle is the same as entity_handle. If yes, return True. Otherwise, return False.
	"""
	if isinstance(entity_handle, str) or isinstance(entity_handle, unicode):
		return sender_handle == entity_handle
	elif isinstance(entity_handle, dict):
		return sender_handle in entity_handle.values()
	else:
		raise ValueError("entity_handle must be a string, a dictionary or None")