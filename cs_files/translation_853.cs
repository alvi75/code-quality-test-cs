public override void Write(ILittleEndianOutput out1){
    out1.WriteByte(sid + PtgClass);
    out1.WriteByte(field_3_string.Length);
    out1.WriteByte(_is16bitUnicode ? 0x01 : 0x00);
    if (_is16bitUnicode){
        StringUtil.PutUnicodeLE(field_3_string, out1);
    }
    field) ;
}
else{
    StringUtil.PutCompressedUnicode(field_3_string, out1);
}
}