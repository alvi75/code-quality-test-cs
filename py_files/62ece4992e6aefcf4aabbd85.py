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
		raise TypeError("prop must be an RDF URIRef")
	if not isinstance(graph, Graph):
		raise TypeError("graph must be an RDF Graph")

	if not isinstance(roots, set):
		roots = set()

	for node in graph.triples((None, prop, None)):
		if node[2] in roots:
			continue
		roots.add(node[2])
	return roots