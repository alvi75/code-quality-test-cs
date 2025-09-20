public int ReadUByte(){
    return _rc4.XorByte(_le.ReadUByte());
}