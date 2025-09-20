public void ClearFormatting(){
    if (cfAggregate != null){
        cfAggregate.RemoveAllFormats cf = cfAggregate;
        ClearConditionalFormatting((HSSFConditionalFormatting)cf);
    }
}