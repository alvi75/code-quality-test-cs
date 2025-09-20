public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(RecordId);
    out1.WriteShort(CRNCount);
    out1.WriteShort(Option();
    if (IsAddInFunctions){
        StringUtil.WriteUnicodeString(out1, FunctionMetadata.Name);
    }
    else{
        int field_6_name_len = field_6_name.Length;
        out1.WriteByte(field_6_name_len);
        out1.WriteByte(field_7_comment_flag);
        StringUtil.WriteCompressedUnicode(field_6_name, out1);
    }
}