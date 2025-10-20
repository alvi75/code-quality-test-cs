def vertex3tuple(vertices):
	"""
	Get 3 points for each vertex of the polygon.
    This will include the vertex and the 2 points on both sides of the vertex
    If the subscript is out of bounds, take the value of index as 0
    Args:
        vertices: vertices to be converted

    Returns:
        A list where the elements of vertices represented by tuple
	"""
	if len(vertices) == 1:
		return [(vertices[0], vertices[0], vertices[0])]
	elif len(vertices) == 2:
		return [(vertices[0], vertices[0], vertices[1]), (vertices[1], vertices[1], vertices[0])]
	else:
		result = []
		for i in range(len(vertices)):
			result.append((vertices[i % len(vertices)], vertices[(i + 1) % len(vertices)],
						   vertices[(i - 1) % len(vertices)]))
		return result