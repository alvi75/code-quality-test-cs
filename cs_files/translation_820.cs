public ExternalBookBlock(int numberOfSheets){
    _externalBookRecord = SupBookRecord.CreateInternalReferences(numberOfSheets);
    _externalNameRecords = new ExternalNameRecord[0];
    _crnBlocks = new CRNBlock[0];
}