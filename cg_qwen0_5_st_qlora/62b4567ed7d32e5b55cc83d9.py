def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for node in nodes:
		if isinstance(node, MappingNode):
			for key, value in node.items():
				if key not in result:
					result[key] = value
				elif isinstance(result[key], MappingNode):
					result[key] = deep_merge_nodes([result[key]])
				else:
					result[key] = [result[key], value]
	return result