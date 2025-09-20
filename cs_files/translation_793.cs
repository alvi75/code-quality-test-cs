public virtual int CompareTo(BytesRef other){
    return utf8SortedAsUnicodeSortOrder.Compare(this, other);
}