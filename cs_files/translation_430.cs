public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(Chart(0));
    out1.WriteShort(1);
    out1.WriteInt(2);
    out1.WriteInt(3);
    out1.WriteShort(4);
    out1.WriteShort(5);
    out1.WriteShort(6);
}