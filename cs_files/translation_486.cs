public static double Floor(double n, double s){
    double c;
    if (s == 0){
        if (n < 0){
            return -Math.Abs(n);
        }
    }
    else{
        return Math.Abs(n);
    }
}
}
double d = (n > 0 && s < 0)? -s: s;
return Math.Floor(n / d) * d;
}