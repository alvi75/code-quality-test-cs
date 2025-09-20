public static NumberRecord ConvertRKRecords(MulRKRecord mrk){
    NumberRecord nr = new NumberRecord();
    nr.Column=(mrk.FirstColumn);
    nr.Row=(mrk.Row);
    nr.XFIndex=(mrk.GetXFAt(0));
    nr.Value=(mrk.RKNumbers[0]);
    int nItems = mrk.NumberOfRichTextRuns;
    for (int i = 1;
    i < nItems;
    i++){
        NumberRecord nrItem = new NumberRecord();
        nrItem.Column=(mrk.GetColumnAt(i));
        nrItem.Row=(mrk.Row);
        nrItem.XFIndex=(mrk.GetXFAt(i));
        nrItem.Value=(mrk.RKNumbers[i]);
        nr.Add(nrItem);
    }
    else{
        nr.IsAddInFunctions = true;
    }
    return nr;
}