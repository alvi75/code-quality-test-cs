public override int Get(int index, long[] arr, int off, int len){
    Debug.Assert(len > 0, "len must be > 0 (got " + len + ")");
    Debug.Assert(index >= 0 && index < valueCount);
    len = Math.Min(len, valueCount - index);
    if (index == 0){
        arr[off] = 1;
    }
    else if ((index - 1) * outerInstance.valueCount >= blockIndex && index <= valueCount){
        long skip = (index - 1) * outerInstance.blockSize;
        outerInstance.blockList.GetBlockAt(skip, arr, off, len);
    }
    else{
        for (int i = off;
        i < off + len;
        ++i){
            arr[i] = 0;
        }
    }
    return len;
}