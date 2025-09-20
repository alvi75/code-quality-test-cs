public void AddShape(HSSFShape shape){
    shape.Patriarch = this;
    shape.Parent = this;
    shapes.Add(shape);
}