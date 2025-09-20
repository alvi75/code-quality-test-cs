public override bool Equals(Object obj){
    if (this == obj)return true;
    if (obj == null)return false;
    if (obj is ExtendedFormatRecord){
        ExtendedFormatRecord other = (ExtendedFormatRecord)obj;
        if (field_1_font_index != other.field_1_font_index)return false;
        if (field_2_format_index != other.field_2_format_index)return false;
        if (field_3_cell_options != other.field_3_cell_options)return false;
        if (field_4_alignment_options != other.field_4_alignment_options)return false;
        if (field_5_indention_options != other.field_5_indention_options)return false;
        if (field_6_border_options != other.field_6_border_options)return false;
        if (field_7_palette_options);
    }