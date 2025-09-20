public SparseIntArray(int capacity){
    if (capacity < 0){
        throw new IllegalArgumentException("Capacity must be >= 0");
    }
    mKeys = new int[capacity];
    mValues = new int[capacity];
    mSize = 0;
}