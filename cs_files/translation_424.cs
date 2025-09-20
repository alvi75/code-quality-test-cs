public override float get(int index){
    checkIndex(index);
    return byteBuffer.getFloat(index * libcore.io.SizeOf.FLOAT);
}