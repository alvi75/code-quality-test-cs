def check_sender_and_entity_handle_match(sender_handle, entity_handle):
	"""
	Check whether sender_handle is the same as entity_handle. If yes, return True. Otherwise, return False.
	"""
	if sender_handle == entity_handle:
		return True
	elif sender_handle.startswith("urn:cts:") or entity_handle.startswith("urn:cts:"):
		return False
	else:
		raise ValueError("Invalid sender/entity handle.")