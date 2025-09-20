public NPOI.SS.UserModel.IColor GetColorColor(byte red, byte green, byte blue){
    byte[] b = palette.GetColor(PaletteRecord.FIRST_COLOR_INDEX);
    short i;
    for (i = PaletteRecord.FIRST_COLOR_INDEX;
    b != null;
    b = palette.GetColor(++i)){
        if (b[0] == red && b[1] == green && b[2] == blue){
            return new CustomColor(i, b);
        }
    }
}
}