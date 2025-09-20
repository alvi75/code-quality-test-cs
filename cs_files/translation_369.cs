public static double kthSmallest(double[] v, int k){
    double r = double.NaN;
    k--;
    if (v != null && v.Length > k && k >= 0){
        Array.Sort(v);
        r = v[v.Length - k - 1];
    }
    return r;
}