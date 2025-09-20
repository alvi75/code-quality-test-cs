public virtual int Get(int i){
    if (count <= i){
        throw new IndexOutOfRangeException(i.ToString());
    }
    return entries[i];
    i;
}