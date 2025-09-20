public MergedCellsTable(RecordStream rs){
    _cfHeaders = new ArrayList<>();
    while (rs.PeekNextSid() == CellRangeAddress.sid){
        CFRecordsAggregate subAgg = (CFRecordsAggregate)rs.GetNext();
        int nRules = subAgg.NumberOfConditionalFormats;
        if (nRules > 0){
            CFRuleBase[] rules = new CFRuleBase[nRules];
            for (int i = 0;
            i < rules.Length;
            i++){
                rules[i] = (CFRuleBase)rs.GetNext();
            }
            _cfHeaders.Add(subAgg);
        }
    }