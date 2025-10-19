def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	result = {}
	for child in node:
		result[child.tag] = child
	return result