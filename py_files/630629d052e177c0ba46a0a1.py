def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""

	if not isinstance(doc, ElementTree.Element):
		doc = ElementTree.fromstring(doc)

	try:
		signature = SignatureElement.from_string(signature)
	except ValueError as e:
		raise InvalidSignature(e.message)

	public_key = PublicKey.from_x509_certificate(
			X509Certificate.from_cryptography_public_key(
				cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicNumbers(
					int(public_key.n),
					int(public_key.e)
				).public_key()
			)
		)

	return signature.verify(
		ElementTree.tostring(doc), public_key,
		hashlib.sha256
	)