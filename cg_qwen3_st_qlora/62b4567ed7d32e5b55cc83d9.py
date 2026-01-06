def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if not nodes:
		return None

	# Merge all nodes into a single one
	result = nodes[0]
	for node in nodes[1:]:
		if isinstance(node, MappingNode):
			# Merge two mappings
			for key_node, value_node in node.value:
				key = key_node.value
				if key in result:
					# Merge two lists
					if isinstance(result[key], SequenceNode) and isinstance(value_node, SequenceNode):
						result[key].value.extend(value_node.value)
					else:
						# Merge two mappings
						if isinstance(result[key], MappingNode) and isinstance(value_node, MappingNode):
							result[key] = deep_merge_nodes([result[key], value_node])
						else:
							# Replace the value
							result[key] = value_node
				else:
					# Add new key-value pair
					result[key_node.value] = value_node
		elif isinstance(node, ScalarNode):
			# Replace the value
			result[node.value] = node
		else:
			raise ValueError("Unexpected node type: %s" % node)

	return result