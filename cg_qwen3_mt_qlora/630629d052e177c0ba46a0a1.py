def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, etree._Element):
		doc = etree.fromstring(doc)
	if not isinstance(signature, etree._Element):
		signature = etree.fromstring(signature)

	try:
		doc.verify_signature(
			public_key,
			signature,
			'urn:ietf:params:xml:ns:xmpp-sasl',
			'auth')
	except Exception as e:
		raise ValueError('Invalid signature: %s' % str(e))
	return True