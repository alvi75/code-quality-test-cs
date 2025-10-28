def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	result = {}
	for n in nodes:
		if isinstance(n, MappingNode):
			for k,v in n.items():
				if k not in result or not isinstance(result[k], MappingNode):
					result[k] = v
				else:
					result[k].merge(v)
	return result