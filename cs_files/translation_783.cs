public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(Height);
    out1.WriteByte(field, Options);
}