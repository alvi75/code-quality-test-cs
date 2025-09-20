public override void Write(char[] b, int off, int len){
    m_buf.CheckCapacity(len);
    UnsafeWrite(b, off, len);
}