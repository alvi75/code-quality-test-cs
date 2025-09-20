public FeatRecord(RecordInputStream in1){
    futureHeader = new FtrHeader(in1);
    isf_sharedFeature = in1.ReadByte();
    reserved1 = (byte)in1.ReadByte();
    reserved2 = in1.ReadInt();
    int cRef = in1.ReadUShort();
    cbFeatData = in1.ReadInt();
    reserved3 = in1.ReadUShort();
    if (cRef != cellRefs.Length){
        _cellRefs = new CellRangeAddress[cRef];
        for (int i = 0;
        i < _cellRefs.Length;
        i++){
            _cellRefs[i] = new CellRangeAddress(in1);
        }
    }
    else{
        _cellRefs = null;
    }
}