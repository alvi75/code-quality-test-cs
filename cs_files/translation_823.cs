public virtual int CompareTo(SearchTimeTracker other){
    return TimeInMilliSeconds - other.TimeInMilliSeconds;
}