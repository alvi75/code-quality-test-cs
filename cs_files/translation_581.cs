public override long RamBytesUsed(){
    long sizeInBytes = 0;
    foreach (FieldIndexData entry in fields.Values){
        sizeInBytes += entry.RamBytesUsed();
    }
    return sizeInBytes;
}