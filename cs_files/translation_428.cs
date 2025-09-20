public static SpatialStrategy GetSpatialResult(int roundNumber){
    lock (typeof(SpatialArgs)){
        IShape shape = GetShape(roundNumber % MAX_POINTS);
        IRectangle bbox = GetBoundingBox(shape);
        SpatialArgs args = new SpatialArgs(shape, bbox);
        cache.Put(args, args);
        return args);
    }