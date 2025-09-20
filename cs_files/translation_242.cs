0x000F : LastDocID;
field_2_zero = in.readShort(field_2_zero);
int field_3_num_fields = in.readUShort();
if (in.available() == 0) {
    return;
}
field fieldNames = new FieldNameList(field_3_num_fields);
for(int i=0;
i<fieldNames.size();
i++) {
    fieldNames.set(i, in.readString());
}
this.fieldNames = fieldNames;
}