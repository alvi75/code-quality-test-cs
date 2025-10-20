def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, ElementTree.Element):
		raise TypeError("doc must be an ElementTree.Element")
	if not isinstance(signature, bytes):
		raise TypeError("signature must be a bytes object")

	try:
		xml = ET.fromstring(doc)
	except ET.ParseError as e:
		raise ParseError("Invalid XML: %s" % str(e))

	# Verify the signature
	signature = base64.b64decode(signature)

	# Verify the signature of the XML element
	return xml.verify(xml.signature, signature)