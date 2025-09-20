public static java.nio.FloatBuffer allocate(int capacity_1){
    if (capacity_1 < 0){
        throw new System.ArgumentException();
    }
    return new java.nio.ReadWriteFloat_128FloatArrayBuffer(capacity_1);
}