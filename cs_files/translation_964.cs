public override java.nio.FloatBuffer slice(){
    return new java.nio.ReadWriteFloat(java.nio.FloatBuffer.copy(this, _mark));
}