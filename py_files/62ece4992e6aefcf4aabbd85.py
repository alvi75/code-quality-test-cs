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
		raise TypeError("prop must be a URIRef")

	if roots is None:
		roots = set()

	for c in list(graph.objects(None, prop)):
		subj_set = set(graph.subjects(prop, c))
		if len(subj_set) == 0:
			roots.add(c)
		else:
			find_roots(graph, prop, subj_set)

	return roots