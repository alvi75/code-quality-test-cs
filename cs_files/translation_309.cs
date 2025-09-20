public override void Decode(byte[] blocks, int blocksOffset, int[] values, int valuesOffset, int iterations){
    if (bitsPerValue > 32){
        throw new System.NotSupportedException("Cannot decode " + bitsPerValue + "-bits values into an int[]");
    }
    for (int i = 0;
    i < iterations;
    ++i){
        long block = ReadInt64(blocks, blocksOffset);
        blocksOffset += 8;
        valuesOffset = Decode(block, values, valuesOffset);
    }
}