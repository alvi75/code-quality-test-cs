public static long GenerationFromSegmentsFileName(string fileName){
    if (fileName.Equals(IndexFileNames.SEGMENTS_GEN, StringComparison.Ordinal)){
        return -1;
    }
    else{
        if (fileName.StartsWith(IndexFileNames.SEGMENTS, StringComparison.Ordinal)){
            return long.Parse(fileName.Substring(1, 9), NumberStyles.HexNumber);
        }
        else{
            throw new System.ArgumentException("fileName \"" + fileName + "\" is not a segments file name");
        }
    }