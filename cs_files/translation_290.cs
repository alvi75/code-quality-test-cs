public StreamIDRecord(RecordInputStream in1){
    id = in1.ReadShort(ID_LENGTH);
}