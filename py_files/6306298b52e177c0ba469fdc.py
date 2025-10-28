def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	xml = {}
	for child in node.childNodes:
		if child.nodeType == child.ELEMENT_NODE:
			tag_name = child.tagName
			xml[tag_name] = xml_children_as_dict(child)
	return xml