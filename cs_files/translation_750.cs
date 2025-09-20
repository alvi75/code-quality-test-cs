public bool HasAll(RevFlagSet set){
    return (flags & set.mask) == set.mask;
}