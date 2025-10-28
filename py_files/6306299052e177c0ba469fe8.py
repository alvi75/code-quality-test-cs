def check_sender_and_entity_handle_match(sender_handle, entity_handle):
	"""
	Check whether sender_handle is the same as entity_handle. If yes, return True. Otherwise, return False.
	"""
	if sender_handle == entity_handle:
		return True

	sender = get_sender_by_handle(sender_handle)
	entity = get_entity_by_handle(entity_handle)

	if sender != None and entity != None:
		if sender.handle == entity.handle:
			return True

	return False