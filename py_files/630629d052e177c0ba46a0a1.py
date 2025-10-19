def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""

	if not isinstance(signature, six.string_types):
		raise ValueError("signature must be a string")

	try:
		s = Signature()
		s.load_string(signature)
	except Exception as e:
		raise VerificationError("Failed to load signature: %s" % str(e))

	return s.verify(doc, public_key)