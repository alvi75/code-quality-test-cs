def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	children = {}
	for child in node:
		if child.tag not in children:
			children[child.tag] = []
		children[child.tag].append(child)
	return children