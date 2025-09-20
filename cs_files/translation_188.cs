public virtual int CompareTo(ScoreTerm other){
    if (this.Boost == other.Boost){
        return TermComp.Compare(other.Bytes, this.Bytes);
    }
    else{
        return this.Boost.CompareTo(other. Boost);
    }
}