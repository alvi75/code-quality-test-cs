def check_sender_and_entity_handle_match(sender_handle, entity_handle):
	"""
	Check whether sender_handle is the same as entity_handle. If yes, return True. Otherwise, return False.
	"""
	if type(entity_handle) != str:
		return False

	if len(entity_handle) == 0:
		return False

	if len(sender_handle) == 0:
		return False

	if (sender_handle[0:len(entity_handle)] == entity_handle):
		return True

	return False