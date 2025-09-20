public override Merger NewMerger(Repository db){
    return new Strategydb3.OneSide(db);
}