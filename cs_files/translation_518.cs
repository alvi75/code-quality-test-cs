public static void StrCpy(char[] dst, int doff, char[] src, int soff){
    while (src[soff] != 0){
        dst[doff++] = src[soff++];
    }
    dst[doff] = (char)0;
}