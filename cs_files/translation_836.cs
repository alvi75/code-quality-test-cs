public override void Decode(byte[] blocks, int blocksOffset, long[] values, int valuesOffset, int iterations){
    for (int i = 0;
    i < iterations;
    ++i){
        long byte0 = blocks[blocksOffset++] & 0xFF;
        long byte1 = blocks[blocksOffset++] & 0xFF;
        values[valuesOffset++] = (byte0 << 4) | ((long)((ulong)byte1 >> 4));
        long byte2 = blocks[blocksOffset++] & 0xFF;
        values[valuesOffset++] = ((byte1 & 15) << 8) | byte2;
    }
}