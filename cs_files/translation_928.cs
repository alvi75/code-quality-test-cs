public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(BarSpace);
    out1.WriteShort(Chart(0));
    out1.WriteShort(BarSpace);
}