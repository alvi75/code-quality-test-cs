public virtual void CopyTo(byte[] b, int o){
    FormatHexByte(b, o, w1);
    FormatHexByte(b, o + 8, w2);
    FormatHexByte(b, o + 16, w3);
    FormatHexByte(b, o + 24, w4);
    FormatHexByte(b, o + 32, w5);
}