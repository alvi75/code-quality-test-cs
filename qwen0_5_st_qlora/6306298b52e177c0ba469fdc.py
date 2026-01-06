def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	dict = {}
	for child in node:
		if child.tag not in dict:
			dict[child.tag] = []
		dict[child.tag].append(child)
	return dict