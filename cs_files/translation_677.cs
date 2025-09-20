public override bool Equals(object o){
    if (this == o){
        return true;
    }
    if (!(o is FacetEntry)){
        return false;
    }
    FacetEntry other = (FacetEntry)o;
    if (Count != other.Count){
        return false;
    }
    int index = 0;
    while (index < Count){
        if (Values[index] != other.Values[index]){
            return false;
        }
        index++;
    }
    return true;
}