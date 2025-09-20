public override java.nio.IntBuffer slice(){
    return new java.nio.ReadOnlyIntArrayBuffer(remaining(), backingArray, offset+ _position);
}