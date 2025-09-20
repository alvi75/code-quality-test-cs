public IPolygon CreatePolygon(IHSSFClientAnchorResponse shape = new HSSFPolygon(null, (HSSFAnchorResponse)anchor);
AddShape(shape);
OnCreate(shape);
return shape;
}