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
        raise TypeError("graph must be a Graph object")

    if not isinstance(roots, set):
        roots = set()

    # get all parents for each node
    parents = defaultdict(set)

    for s, p, o in graph.triples((None, prop, None)):
        parents[o].add(s)

    # find root by looking for no parents
    for n in graph.subjects(RDF.type, None):
        if len(parents[n]) == 0:
            roots.add(n)

    return roots