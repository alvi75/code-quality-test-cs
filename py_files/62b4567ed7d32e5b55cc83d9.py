def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for node in nodes:
		if isinstance(node, MappingNode):
			for key, value in node.value.items():
				if key not in result:
					result[key] = value
				else:
					if isinstance(result[key], MappingNode) and isinstance(value, MappingNode):
						result[key] = deep_merge_nodes([result[key], value])
					else:
						result[key] = value
	return result