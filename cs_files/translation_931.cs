public static int Match(byte[] b, int ptr, byte[] src){
    if (ptr + src.Length > b.Length){
        return -1;
    }
    for (int i = 0;
    i < src.Length;
    i++){
        if (b[ptr++] != src[i]){
            return -1;
        }
    }
}
}