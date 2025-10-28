def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		raise TypeError("doc must be an ElementTree.Element instance")
	if not isinstance(signature, bytes):
		raise TypeError("signature must be a bytes object")

	try:
		xml = etree.tostring(doc)
	except Exception as e:
		raise ValueError("Failed to serialize document: %s" % str(e))

	return _verify_relayable_signature(public_key, xml, signature)