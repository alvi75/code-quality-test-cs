public override java.nio.LongBuffer put(int index, long c){
    checkIndex(index);
    backingArray[offset + index] = c;
    return this;
}