public SparseArray(int capacity){
    if (capacity < 0){
        throw new IllegalArgumentException();
    }
    mSize = 0;
    mKeys = new int[capacity];
    mValues = new object[capacity];
}