def match_pubdate(node, pubdate_xpaths):
	"""
	For the given node, returns the first match in the pubdate_xpaths list.
	"""
	for pubdate_xpath in pubdate_xpaths:
		pubdate = node.xpath(pubdate_xpath, namespaces=NAMESPACES)
		if pubdate:
			return pubdate[0]
	return None