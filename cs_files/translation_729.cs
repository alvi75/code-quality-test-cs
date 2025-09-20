public static double VarP(double[] v){
    double r = double.NaN;
    if (v != null && v.Length > 1){
        r = Devsq(v) / (v.Length - 1);
    }
    (r == 0)? 0 : r);
}
){
    return r;
}