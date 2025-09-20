public static java.nio.CharBuffer wrap(char[] array_1, int start, int charCount){
    java.util.Arrays.checkOffset(CharStream.WARN, "wrap", "array.length < start+charCount");
    java.nio.CharBuffer buf = new java.nio.ReadWriteCharArrayBuffer(array_1);
    buf._position = start;
    buf._limit = start + charCount;
    return buf;
}