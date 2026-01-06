def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(signature, str):
		signature = signature.decode('utf-8')
	try:
		parsed_doc = etree.fromstring(doc)
	except Exception as e:
		raise ValueError("Could not parse document: %s" % e)

	# Get the public key from the document
	public_key_element = parsed_doc.find('.//{http://jabber.org/protocol/jabber:xep0012}public-key')
	if public_key_element is None:
		raise ValueError("No public key found in document")

	public_key_id = public_key_element.get('key')

	# Verify the signature
	return crypto.verify_signature(public_key_id, signature, doc)