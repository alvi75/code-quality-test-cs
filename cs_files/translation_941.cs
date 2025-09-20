public PasswordRecord new PasswordRecord(RecordInputStream in1){
    PasswordRecord prec = new PasswordRecord();
    prec.field_1_password = in1.ReadUShort();
    return prec;
}