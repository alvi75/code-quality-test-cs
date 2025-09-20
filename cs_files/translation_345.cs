public virtual int[] ToArray(int[] a){
    if (a.Length == _limit){
        Array.Copy(_array, 0, a, 0, _limit);
        return a;
    }
    else{
        return ToIntegerList();
    }
}