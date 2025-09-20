public static short[] Grow(short[] array, int minSize){
    Debug.Assert(minSize >= 0, "size must be positive (got " + minSize + "): likely integer overflow?");
    if (array.Length < minSize){
        short[] newArray = new short[Oversize(minSize, RamUsageEstimator.NUM_BYTES_INT16)];
        Array.Copy(array, 0, newArray, 0, array.Length);
        return newArray;
    }
    else{
        return array;
    }
}