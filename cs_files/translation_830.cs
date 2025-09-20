public EscherGraphics(HSSFShapeGroup escherGroup, HSSFWorkbook workbook, IFont font, byte[] foreground){
    this.m_hescherGroup = escherGroup;
    this.m_workbook = workbook;
    this.font = font;
    this.foreground = foreground;
}