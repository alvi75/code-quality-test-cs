public ShapeFieldCacheDistanceValueSource(SpatialContext ctx, IShapeFieldCacheProvider shapeFieldCacheProvider, IPoint from, double multiplier){
    this.m_ctx = ctx;
    this.m_shapeFieldCacheProvider = shapeFieldCacheProvider;
    this.m_from = from;
    this.m_multiplier = multiplier;
}