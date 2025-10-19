def _parse_document(document):
		try:
			return json.loads(document)
		except Exception as e:
			raise DiasporaWebFingerParsingError("Failed to parse Diaspora WebFinger document", e)

	document = _parse_document(document)
	if "hcard_url" not in document or "href" not in document["hcard_url"]:
		raise DiasporaWebFingerParsingError("Invalid Diaspora WebFinger document")
	return {"webfinger": document["hcard_url"]["href"]}