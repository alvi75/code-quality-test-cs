public void AddMultipleBlanks(MulBlankRecord mbr){
    for (int k = 0;
    k < mbr.NumColumns;
    k++){
        BlankRecord br = new BlankRecord();
        br.Column = ((short)(k + mbr.FirstColumn));
        br.Row = mbr.Row;
        br.XFIndex = mbr.GetXFAt(k);
        AddCell(br);
    }
}
}
}