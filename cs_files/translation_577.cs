public virtual bool Contains(char[] text, int offset, int length){
    return map.ContainsKey(text, offset, length);
}