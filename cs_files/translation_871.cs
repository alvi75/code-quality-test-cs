public ColumnInfoRecord(RecordInputStream in1){
    this.ColumnWidth = in1.ReadUShort();
    this.XFIndex = in1.ReadUShort();
    int cchName = in1.ReadUShort();
    if (cchName != STRING_NOT_PRESENT_LEN){
        this.ColumnName = in1.ReadUnicodeLEString(cchName);
    }
    else{
        this.ColumnName = "";
    }
}