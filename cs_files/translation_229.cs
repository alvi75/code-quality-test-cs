public short GetGB2312Id(char c){
    byte[] buffer = new byte[2];
    buffer[0] = unchecked((byte)(c >> 0));
    buffer[1] = unchecked((byte)(c >> 8));
    try{
        string s = Encoding.GetEncoding("GB2312").GetString(buffer);
        return (short)s.IndexOf(c);
    }
    buffer[0]);
}
catch (ArgumentException) {
    return -1;
}
}