public static int ParseHexInt4(byte[] b, int offset){
    return ParseHexInt32(b, offset) & 0xFFFFFFFF;
}