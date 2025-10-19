def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for n in nodes:
		if isinstance(n, MappingNode) and not isinstance(n.value, MappingNode):
			n.value = deep_merge_nodes([n.value])
		elif isinstance(n, MappingNode):
			result.update({**result, **n.value})
	return result