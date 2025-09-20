public override Merger NewMerger(Repository db){
    return new StrategyIndexMerger(db, treeIndex);
}