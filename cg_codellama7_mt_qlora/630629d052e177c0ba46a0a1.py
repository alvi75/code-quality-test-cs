def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	if not isinstance(doc, etree._Element):
		doc = etree.fromstring(doc)
	if not isinstance(signature, etree._Element):
		signature = etree.fromstring(signature)
	if not isinstance(public_key, etree._Element):
		public_key = etree.fromstring(public_key)
	if not isinstance(signature, etree._Element):
		raise ValueError("Signature must be an Element")
	if not isinstance(public_key, etree._Element):
		raise ValueError("Public key must be an Element")
	if not isinstance(doc, etree._Element):
		raise ValueError("Document must be an Element")
	if not signature.tag == "Signature":
		raise ValueError("Signature must be a Signature element")
	if not public_key.tag == "X509Data":
		raise ValueError("Public key must be an X509Data element")
	if not doc.tag == "Envelope":
		raise ValueError("Document must be an Envelope element")
	if not signature.find("./SignedInfo/CanonicalizationMethod").text == "http://www.w3.org/2001/10/xml-exc-c14n#":
		raise ValueError("Canonicalization method must be http://www.w3.org/2001/10/xml-exc-c14n#")
	if not signature.find("./SignedInfo/SignatureMethod").text == "http://www.w3.org/2000/09/xmldsig#rsa-sha1":
		raise ValueError("Signature method must be http://www.w3.org/2000/09/xmldsig#rsa-sha1")
	if not signature.find("./SignedInfo/Reference").text ==