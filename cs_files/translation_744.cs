0x0f, 0x3b, 0x3c, 0x58, 0x93, 0x6c, 0x6a, 0x16, 0x01);
int pos = 0;
LittleEndian.PutInt(data, pos, Options);
pos += 2;
LittleEndian.PutInt(data, pos, RecordId);
pos += 4;
LittleEndian.PutInt(data, pos, PropertiesSize);
pos += 4;
for (IEnumerator iterator = properties.GetEnumerator();
iterator.MoveNext();
){
    EscherProperty property = (EscherProperty)iterator.Current;
    pos += property.Serialize(pos, data, listener);
}
else{
    listener.AfterRecordSerialize(pos, RecordId, pos - offset, this);
    return pos - offset;
}
}