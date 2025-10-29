def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
	"""
	 Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader

    Args:
        graph: Graph Class Object
        prop: URIRef Class Object
        roots: Optional list with set type
    Return:
        roots: a set with nodes
	"""
	if not isinstance(prop, URIRef):
		raise TypeError("prop must be an RDF.URIRef")
	if not isinstance(graph, Graph):
		raise TypeError("graph must be a Graph")

	if not roots:
		roots = set()

	for node in graph.subjects(RDF.type, prop):
		if node not in graph.objects(node, prop):
			continue
		for child in graph.objects(node, prop):
			if child not in graph.objects(child, prop):
				continue
			if child not in graph.objects(child, RDF.type):
				continue
			if child not in graph.objects(child, RDF.type, prop):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if child not in graph.objects(child, RDF.type, prop, context=graph):
				continue
			if