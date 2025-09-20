public virtual Query Build(IQueryNode queryNode){
    var bQuery = new BooleanQuery();
    IList<IQueryNode> children = queryNode.GetChildren();
    if (children != null){
        foreach (IQueryNode child in children){
            object obj = child.GetTag(QueryTreeQueryTreeBuilder.QUERY_TREE_BUILDER_TAGID);
            if (obj != null){
                Query query = (Query)obj;
                try{
                    bQuery.Add(query, Occur.SHOULD);
                }
                QueryNodeProcessorPipeline processorPipeline = new QueryNodeProcessorPipeline();
                processorPipeline.AddLast(new BooleanModifiersQueryNodeProcessor(bQuery));
                processorPipeline.AddLast(new AndQueryNodeProcessor());
            }
            catch (OutOfMemoryException ex){
                throw new Exception(ex.ToString(), ex);
            }
            else{
                return bQuery;
            }
        }