public virtual int FindEndOffset(StringBuilder buffer, int start){
    if (start > buffer.Length || start < 0) return start;
    int offset, count = m_maxScan;
    for (offset = start;
    offset < buffer.Length && count > 0;
    count--){
        if (m_boundaryChars.Contains(buffer[offset])) return offset;
    }
    return start;
}