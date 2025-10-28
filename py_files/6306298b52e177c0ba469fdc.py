def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	return {child.tag: xml_child_as_dict(child) for child in node}