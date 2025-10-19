def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		doc = ElementTree.fromstring(doc)
	signature = base64.b64decode(signature)

	try:
		pkcs7 = PKCS7()
		pkcs7.parse(doc)
	except TypeError as e:
		return False

	if pkcs7.certificates is None or len(pkcs7.certificates) == 0:
		return False

	for cert in pkcs7.certificates:
		if cert.signature is None:
			continue
		if cert.signature.base64() != signature:
			return False

	return True