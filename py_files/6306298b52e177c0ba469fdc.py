def xml_children_as_dict(node):
	"""
	Turn the children of node <xml> into a dict, keyed by tag name.
	"""
	d = {}
	for child in node:
		if child.tag == 'xml':
			continue
		tag_name = child.tag
		if tag_name not in d:
			d[tag_name] = []
		d[tag_name].append(child)
	return d