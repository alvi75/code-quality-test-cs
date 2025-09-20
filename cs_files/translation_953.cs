public FRTInfoRecord(RecordInputStream in1){
    rt = in1.ReadUShort();
    grbitFrt = in1.ReadUShort();
    verOriginator = in1.ReadByte();
    verWriter = in1.ReadByte();
    int cCFRTID = in1.ReadUShort();
    rgCFRTID = new CFRTID[cCFRTID];
    for (int i = 0;
    i < cCFRTID;
    i++){
        rgCFRTID[i] = new CFRTID(in1);
    }
}