def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		doc = ElementTree.fromstring(doc)
	if not isinstance(signature, ElementTree.Element):
		signature = ElementTree.fromstring(signature)

	# Verify the signature
	try:
		ElementTree.XMLSignature.verify(
			signature,
			doc,
			public_key=public_key,
			keyname='rsa',
			certname='rsa'
		)
	except Exception as e:
		raise InvalidSignatureError(e)

	return True