def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	ret = {}
	for child in node.iterchildren():
		if child.tag not in ret:
			ret[child.tag] = []
		ret[child.tag].append(child.text)
	return ret