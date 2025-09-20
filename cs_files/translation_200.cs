public void Write(int b){
    CheckPosition(1);
    _buf[_writeIndex++] = (byte)b;
}