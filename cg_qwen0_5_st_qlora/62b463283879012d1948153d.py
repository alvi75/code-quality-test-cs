def match_pubdate(node, pubdate_xpaths):
	"""
	For the given node, returns the first match in the pubdate_xpaths list.
	"""
	for xpath in pubdate_xpaths:
		if node.xpath(xpath) is not None:
			return True
	return False