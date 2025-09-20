public override String ToString(){
    StringBuilder buffer.Append("[CHART]\n");
    String[] seriesNames = chartGroup.SeriesToChartGroup.Keys.ToArray();
    for (int i = 0;
    i < seriesNames.Length;
    i++){
        SeriesToChartGroup smg = (SeriesToChartGroup)chartGroup.SeriesToChartGroup[seriesNames[i]];