public override long RamBytesUsed(){
    long sizeInByes = 0;
    foreach (FieldIndexData entry in fields.Values){
        sizeInByes += entry.RamBytesUsed();
    }
    return sizeInByes;
}