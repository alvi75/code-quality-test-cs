static public double PMT(double r, int nper, double pv, double fv, int type){
    double retval = 0;
    if (r == 0){
        retval = -1*(fv+(pv*Math.Pow(1+r, nper)))/nper;
    }
    else{
        double r1 = r + 1;
        retval = -(fv + pv * Math.Pow(r1, nper)) * r/((Math.Pow(r1, nper) - 1) * (type==1 ? r1 : 1));
    }
    return retval;
}