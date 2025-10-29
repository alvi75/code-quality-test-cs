def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		raise TypeError("doc must be an ElementTree.Element object")
	if not isinstance(signature, bytes):
		raise TypeError("signature must be a bytes object")

	# Verify the signature
	try:
		signature = base64.b64decode(signature)
	except TypeError:
		raise TypeError("signature must be a bytes object")

	try:
		public_key.verify(signature, doc)
	except (ValueError, TypeError) as e:
		raise ValueError("Invalid signature: %s" % str(e))