public virtual int FindEndOffset(StringBuilder buffer, int start){
    if (start > buffer.Length || start < 0) return start;
    bi.SetText(buffer.ToString(start, buffer.Length - start));
    bi.Last();
    return bi.Previous();
}