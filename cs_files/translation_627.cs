public override void Serialize(ILittleEndianOutput out1){
    out1.WriteShort(FirstRowGutter);
    out1.WriteShort(GutterWidth);
    out1.WriteShort(FirstColumnGutter);
    out1.WriteShort(FirstRowGroup);
    out1.WriteShort(NumDbcellsPerBlock);
    out1.WriteInt(Option(2));
}