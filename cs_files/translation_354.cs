public override void Write(int b){
    Debug.Assert(slice != null);
    if (slice[upto] != 0){
        p = upto & (blockSize - 1);
        p = p == 0 ? 64 : p;
        buffer[p++] = (byte)b;
        return;
    }
    int oldLen = buffer.Length;
    buffer = ArrayUtil.Grow(buffer, 1 + count);
    count += WriteContinueIfRequired(oldLen);
    buffer[count - 1] = unchecked((byte)b);
    upto = count;
}