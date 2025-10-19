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
    if not isinstance(graph, Graph):
        raise TypeError("graph must be a graph")

    if roots is None:
        roots = set()
    else:
        try:
            roots.add(set())
        except AttributeError:
            raise TypeError("roots must be a set")

    for node in graph.objects(rdflib.URIRef(prop), RDF.type):
        if node == rdflib.URIRef(RDF.nil):
            continue
        if node not in roots:
            roots.add(node)
            find_roots(graph, node, roots)

    return roots