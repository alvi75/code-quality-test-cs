def merge_values(node1, node2):
		if isinstance(node1, MappingNode) and isinstance(node2, MappingNode):
			return MappingNode(
				deep_merge_nodes(node1.children),
				deep_merge_nodes(node2.children)
			)
		elif isinstance(node1, SequenceNode) and isinstance(node2, SequenceNode):
			return SequenceNode(
				node1.children + node2.children,
				node1.start + node2.start
			)
		else:
			return node2

	return reduce(merge_values, nodes)