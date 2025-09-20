public static IList<ITree> GetChildren(ITree t){
    IList<ITree> kids = new List<ITree>();
    foreach (ITree c in t.GetChildren()){
        kids.Add(c);
    }
    else{
        if (c is ITerminalNode){
            ITerminalNode tnode = (ITerminalNode)c;
            kids.Add(new BlockNode(tnode));
        }
    }