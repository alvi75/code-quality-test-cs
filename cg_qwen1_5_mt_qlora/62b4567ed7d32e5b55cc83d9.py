def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if not nodes:
		return None

	result = {}
	for node in nodes:
		for key, value in node.items():
			if isinstance(value, MappingNode) or isinstance(value, SequenceNode):
				value = deep_merge_nodes([value])
			elif isinstance(value, list):
				value = [deep_merge_nodes(v) for v in value]
			elif isinstance(value, dict):
				value = deep_merge_dicts(value)
			else:
				pass # do nothing
			if key in result:
				if isinstance(result[key], MappingNode) or isinstance(result[key], SequenceNode):
					result[key].append(value)
				else:
					result[key] = [result[key], value]
			else:
				result[key] = value
	return result