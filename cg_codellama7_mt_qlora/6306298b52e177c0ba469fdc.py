def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	d = {}
	for child in node.children:
		if child.tag in d:
			d[child.tag].append(child)
		else:
			d[child.tag] = [child]
	return d