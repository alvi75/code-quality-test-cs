public virtual java.nio.ByteBuffer Read(int length, long position){
    if (position >= size()){
        throw new System.IndexOutOfRangeException("Position " + position + " past the end of the file");
    }
    java.nio.ByteBuffer dst = (_writable ? _channel.Map<FileChannel.OpenMode>(FileChannel.OpenModes.ReadWrite, position, length) : _channel.ReadDirect(position, length));
    _buffersToClean.Add(dst);
    return dst;
}