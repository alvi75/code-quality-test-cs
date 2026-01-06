def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if not isinstance(nodes, (list, tuple)):
		nodes = [nodes]
	return _deep_merge_nodes(nodes)