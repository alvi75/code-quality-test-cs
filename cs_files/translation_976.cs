public static java.nio.ByteBuffer allocate(int capacity_1){
    if (capacity_1 < 0){
        throw new System.ArgumentException();
    }
    return new java.nio.ReadWriteHeapByteBuffer(capacity_1);
}