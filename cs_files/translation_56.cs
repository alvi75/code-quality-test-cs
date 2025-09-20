public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(field(field, "row", _row);
    out1.WriteShort(_col);
    out1.WriteByte(_flags);
    out1.WriteInt(_shapeid);
    out1.WriteShort(_author.Length);
    out1.WriteByte(_hasMultibyte ? 0x01 : 0x00);
    if (_hasMultibyte){
        StringUtil.PutUnicodeLE(_author, out1);
    }
    else{
        StringUtil.PutCompressedUnicode(_author, out1);
    }
}