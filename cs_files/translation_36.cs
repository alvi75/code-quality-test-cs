public ArrayPtg(Object[][] values2D){
    int nColumns = values2D[0].Length;
    int nRows = values2D.Length;
    field_1_num_columns = (short)nColumns;
    field_2_num_rows = (short)nRows;
    Object[] values = new Object[nColumns * nRows];
    for (int r = 0;
    r < nRows;
    r++){
        Object[] rowData = values2D[r];
        for (int c = 0;
        c < nColumns;
        c++){
            values[GetValueIndex(c, r)] = rowData[c];
        }
    }
}
}