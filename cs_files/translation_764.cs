public QueryNodeProcessor Set(int index, IQueryNodeProcessor processor){
    IQueryNodeProcessor oldProcessor = this.processors[index];
    return processorsQueryConfig(0, size(), processor);
}