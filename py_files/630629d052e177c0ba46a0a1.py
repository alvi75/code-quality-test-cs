def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
	author did actually generate this message.
	"""
	if not isinstance(signature, str):
		raise TypeError("signature must be a string")
	if len(signature) != 128:
		raise ValueError("signature must be exactly 128 bytes long")

	try:
		public_key = PublicKey.from_string(public_key)
	except Exception as e:
		raise ValueError("invalid public key: %s" % e)

	doc = etree.fromstring(doc.encode('utf-8'))
	signature = Signature.from_bytes(signature)
	return public_key.verify(doc, signature)