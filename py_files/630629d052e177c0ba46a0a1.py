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
			public_key,
			'rsa-sha256',
		)
	except Exception as e:
		raise InvalidSignatureError('Invalid signature: %s' % str(e))

	# Check for a valid timestamp
	timestamp = doc.find('{%s}timestamp' % ns['sig'])
	if timestamp is None:
		raise MissingTimestampError('Missing timestamp element')
	if not is_valid_timestamp(timestamp.text):
		raise InvalidTimestampError('Invalid timestamp')