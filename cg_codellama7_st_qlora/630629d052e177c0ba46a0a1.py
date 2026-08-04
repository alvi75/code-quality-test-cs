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
		raise TypeError("signature must be an Element")
	if not isinstance(public_key, etree._Element):
		raise TypeError("public_key must be an Element")
	if not isinstance(doc, etree._Element):
		raise TypeError("doc must be an Element")
	if not isinstance(signature.text, basestring):
		raise TypeError("signature.text must be a string")
	if not isinstance(public_key.text, basestring):
		raise TypeError("public_key.text must be a string")
	if not isinstance(doc.text, basestring):
		raise TypeError("doc.text must be a string")
	if not isinstance(signature.tag, basestring):
		raise TypeError("signature.tag must be a string")
	if not isinstance(public_key.tag, basestring):
		raise TypeError("public_key.tag must be a string")
	if not isinstance(doc.tag, basestring):
		raise TypeError("doc.tag must be a string")
	if not isinstance(signature.attrib, dict):
		raise TypeError("signature.attrib must be a dict")
	if not isinstance(public_key.attrib, dict):
		raise TypeError("public_key.attrib must be a dict")
	if not isinstance(doc.attrib, dict):
		raise TypeError("doc.attrib must be a dict")
	if not isinstance(signature.text