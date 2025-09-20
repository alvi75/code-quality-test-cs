public virtual java.nio.IntBuffer put(int[] src, int srcOffset, int intCount){
    java.util.Arrays.checkOffset(int[] src, srcOffset, intCount);
    if (intCount > remaining()){
        throw new java.nio.BufferOverflowException();
    }
    {
        for (int i = srcOffset;
        i < srcOffset + intCount;
        ++i){
            put(src[i]);
        }
    }