public static double CalcDistanceFromErrPct(IShape shape, double distErrPct, SpatialContext ctx){
    var bbox = shape.BoundingBox;
    if (distErrPct < 0 || distErrPct > 0.5){
        throw new ArgumentException("distErrPct " + distErrPct + " must be between [0 to 0.5]");
    }
    if (distErrPct == 0 || shape is IPoint){
        return 0;
    }
    IRectangle bbox = shape.BoundingBox;
    IList<ITuple<double, double>> points = new List<ITuple<double, double>>(4);
    points.Add(new Tuple<double, double>(bbox.MinX, bbox.MinY));
    points.Add(new Tuple<double, double>(bbox.MaxX, bbox.MinY));
    points.Add(new Tuple<double, double>(bbox.MinX, bbox.MaxY));
    points.Add(new Tuple<double, double>(bbox.MaxX, bbox.MaxY));
    double diagonalDist = ctx.DistCalc.Distance(shape.Center, bbox.MaxX, bbox.MinY);
    return diagonalDist * distErrPct;
}