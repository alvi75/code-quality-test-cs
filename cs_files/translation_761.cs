public void Construct(CellValueRecordInterface rec, RecordStream rs, SharedValueManager sfr){
    if (rec is FormulaRecordAggregate){
        FormulaRecordAggregate fra = (FormulaRecordAggregate)rec;
        SupBookRecord supbook = (SupBookRecord)rs.GetNext();
        int nNames = supbook.NumberOfNames;
        int nUniqueNames = CountUniqueNames(supbook.NameRecords);
        if (nNames > 255 || nUniqueNames > 255){
            throw new Exception("SupBookRecord has invalid field values");
        }
        else if (nNames < 255 && nUniqueNames < 255){
            ((FormulaRecordAggregate)rec).SetNumberOfNames(nNames + 1);
        }
        else{
            if (nNames > 255){
                throw new Exception("Too many name records for this file - must be <= 255");
            }
            if (nUniqueNames > 255){
                throw new Exception("Too many unique name records for this file - must be <= 255");
            }
        }
        NameRecord[] unfilteredNames = new NameRecord[nNames];
        for (int i = 0;
        i < nNames;
        i++){
            unfilteredNames[i] = (NameRecord)rs.GetNext();
        }
        NameRecord[] filteredNames = FilterNames(unfilteredNames, nNames, nUniqueNames);
        if (filteredNames.Length != 255){
            throw new Exception("Expected 255 name records but got " + filteredNames.Length + ".");
        }
        for (int i = 0;
        i < 255;
        i++){
            if (filteredNames[i] == null){
                throw new Exception("Missing name record with index " + i);
            }
        }
        SetCellValueRecord(_definedNamesRecord, _definedNames);
    }