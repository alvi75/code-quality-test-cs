def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if not nodes:
		return None

	# Sort by key length so that longer keys are merged first.
	nodes = sorted(nodes, key=lambda n: len(n.key))

	# Merge all nodes into a single dictionary.
	result = {}
	for node in nodes:
		if node.key in result:
			# If the value is a MappingNode, merge it recursively.
			if isinstance(result[node.key], MappingNode) and isinstance(node.value, MappingNode):
				result[node.key] = deep_merge_nodes([result[node.key], node.value])
			else:
				# Otherwise, just replace the value.
				result[node.key] = node.value
		else:
			# Otherwise, add the new key-value pair.
			result[node.key] = node.value

	return result