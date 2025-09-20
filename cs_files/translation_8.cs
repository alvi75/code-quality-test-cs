public override void Init(int address){
    slice = pool.Buffers[address >> ByteBlockPool.BYTE_BLOCK_SHIFT];
    Debug.Assert(slice != null);
    upto = address & ByteBlockPool.BYTE_BLOCK_MASK;
    offset0 = address;
    Debug.Assert(upto < slice.Length);
}