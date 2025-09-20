public override int[] Grow(){
    Debug.Assert(m_bytesStart != null, "bytesStart is null - not initialized");
    int[] ord = new int[m_initSize];
    System.Array.Copy(m_bytesStart, 0, ord, 0, m_initSize);
    m_bytesStart = ord;
}