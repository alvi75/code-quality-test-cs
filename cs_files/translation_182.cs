public static double DevSq(double[] v){
    double r = double.NaN;
    if (v != null && v.Length >= 1){
        double m = 0;
        double s = 0;
        int n = v.Length;
        for (int i = 0;
        i < n;
        i++){
            s += v[i];
        }
        m = s / n;
        s = 0;
        for (int i = 0;
        i < n;
        i++){
            s += (v[i] - m) * (v[i] - m);
        }
        r = (n == 1) ? 0 : s;
    }
    return r;
}