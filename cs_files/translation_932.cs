public override int FillFields(byte[] data, int offset, IEscherRecordFactory recordFactory){
    int bytesRemaining = ReadHeader(data, offset);
    int pos = offset + 8;
    int size = 0;
    field_1_rectX1 = LittleEndian.GetInt(data, pos + size);
    size += 4;
    field_2_rectY1 = LittleEndian.GetInt(data, pos + size);
    size += 4;
    field_3_rectX2 = LittleEndian.GetInt(data, pos + size);
    size += 4;
    field_4_rectY2 = LittleEndian.GetInt(data, pos + size);
    size += 4;
    if (bytesRemaining != size){
        throw new RecordFormatException("Expected no remaining bytes but got " + bytesRemaining +" (resource id=" + RecordId + ")");
    }
    return 8 + size;
}