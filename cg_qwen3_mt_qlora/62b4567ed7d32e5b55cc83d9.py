def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if len(nodes) == 0:
		return None

	if len(nodes) == 1:
		return nodes[0]

	# Sort by key length so that longer keys are merged first (e.g. "a" < "ab")
	nodes = sorted(nodes, key=lambda n: len(n.key))

	merged = OrderedDict()
	for node in nodes:
		key = node.key
		value = node.value

		if isinstance(value, MappingNode):
			# Recursively merge child nodes
			value = deep_merge_nodes(value.children)

		if key in merged:
			# Merge existing value with new value
			existing_value = merged[key]
			if isinstance(existing_value, MappingNode):
				# Merge two MappingNodes
				merged[key] = deep_merge_nodes([existing_value, value])
			else:
				# Replace a single value with a MappingNode
				merged[key] = MappingNode(children=[existing_value, value])
		else:
			# Add a new value
			merged[key] = value

	return MappingNode(children=list(merged.values()))