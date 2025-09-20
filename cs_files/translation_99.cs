public override Object Clone(){
    NumberFormatIndexRecord rec = new NumberFormatIndexRecord();
    rec.fieldIndex = fieldIndex;
    return rec;
}