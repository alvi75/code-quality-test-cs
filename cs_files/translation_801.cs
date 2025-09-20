public static Record CreateSingleRecord(RecordInputStream in1){
    I_RecordCreator constructor = _recordCreatorsById[(short)in1.Sid];
    if (constructor == null){
        return new UnknownRecord(in1);
    }
    else{
        return constructor.Create(in1);
    }
}