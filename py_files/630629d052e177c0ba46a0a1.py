def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		doc = parseString(ET.tostring(doc))

	if not isinstance(signature, ElementTree.Element):
		signature = parseString(signature)

	# Verify each of the signatures in the document
	for node in doc.findall('.//{http://www.w3.org/2000/09/xmldsig#}Signature'):
		# Get the key info for the signature
		key_info = node.find('./{%s}KeyInfo' % NS['ds'])
		if key_info is None:
			continue

		# Find the RSAKeyValue element
		rsa_key_value = key_info.find('./{%s}RSAKeyValue' % NS['ds'])
		if rsa_key_value is None:
			continue

		# Find the modulus and exponent elements
		modulus = rsa_key_value.find('./{%s}Modulus' % NS['ds'])
		exponent = rsa_key_value.find('./{%s}Exponent' % NS['ds'])

		if modulus is None or exponent is None:
			continue

		# Get the values from the key value nodes
		modulus = base64.b64decode(modulus.text)
		exponent = base64.b64decode(exponent.text)

		# Create a public key object
		public_key_object = RSA.construct((modulus, exponent))

		# Get the signed info
		signed_info = node.find('./{%s}SignedInfo' % NS['ds'])
		if signed_info is None:
			continue

		# Get the canonicalization method
		canonicalization_method = signed_info.find('./{%s}CanonicalizationMethod' % NS['ds'])
		if canonicalization_method is None:
			continue

		# Get the digest method
		digest_method = signed_info.find('./{%s}DigestMethod' % NS['ds'])
		if digest_method is None:
			continue

		# Get the reference elements
		ref_elements = signed_info.findall('./{%s}Reference' % NS['ds'])
		if ref_elements is None:
			continue

		# Get the signature value
		signature_value = node.find('./{%s}SignatureValue' % NS['ds'])
		if signature_value is None:
			continue