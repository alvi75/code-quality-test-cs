public sealed override short get(int index){
    checkIndex(index);
    return backingArray[offset + index];
}