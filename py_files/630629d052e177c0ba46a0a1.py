def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, Element):
		raise ValueError("doc must be an Element")
	if not isinstance(signature, bytes):
		raise ValueError("signature must be a bytes object")

	try:
		xml = etree.fromstring(doc)
	except etree.XMLSyntaxError as e:
		raise ValueError("Invalid XML: %s" % str(e))

	try:
		xml.verify(public_key)
	except Exception as e:
		raise ValueError("Signature verification failed: %s" % str(e))