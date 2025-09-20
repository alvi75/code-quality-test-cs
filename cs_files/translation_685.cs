public static int TrimTrailingWhitespace(byte[] raw, int start, int end){
    int ptr = end - 1;
    while (start < ptr && IsWhitespace(raw[ptr])){
        ptr--;
    }
    return ptr + 1;
}