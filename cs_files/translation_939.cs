public BlankRecord(RecordInputStream in1){
    field_1_row = in1.ReadUShort();
    field_2_col = in1.ReadShort(in1);
    field_3_xf_index = in1.ReadShort(in1);
}