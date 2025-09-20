public override void Next(int delta){
    while (--delta >= 0){
        if (currentSubtree != null){
            ptr += currentSubtree.GetEntrySpan();
        }
        else{
            ptr++;
        }
        ParseEntry();
    }
    throw new ArgumentException("delta must be non-negative");
}