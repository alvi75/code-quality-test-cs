def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if not nodes:
		return None

	result = {}
	for node in nodes:
		if isinstance(node, MappingNode):
			result.update(node)
		else:
			raise TypeError("Expected a MappingNode, got %s" % type(node))

	return result