public static byte[] GetToUnicodeLE(String value){
    byte[] retval = new byte[value.Length * 2];
    for (int k = 0;
    k < value.Length;
    k++){
        char c = value[k];
        retval[k] = unchecked((byte)c);
    }
    retval[k + 1] = unchecked((byte)(c >> 8));
}
return retval;
}