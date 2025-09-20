public virtual ParseTreeMatch Match(IParseTree tree, IParseTree pattern){
    var labels = new Dictionary<string, IParseTree>();
    IPLabels = labels;
    var mismatchedNode = MatchImpl(tree, tree.GetToken (0), labels);
    return new ParseTreeMatch(tree, labels, mismatchedNode);
}