public virtual void ReadBytes(byte[] b, int offset, int len, bool useBuffer){
    var bytesRemaining = _reader.Available();
    if (bytesRemaining < len){
        _in.Read(b, offset, bytesRemaining);
        offset += bytesRemaining;
        len -= bytesRemaining;
        Debug.Assert(!useBuffer || buffer.Length >= len);
    }
    _in.Read(b, offset, len);
}