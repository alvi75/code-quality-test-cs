public static double Max(double[] values){
    double max = double.MinValue;
    for (int i = 0, iSize = values.Length;
    i < iSize;
    i++){
        max = Math.Max(max, values[i]);
    }
    return max;
}