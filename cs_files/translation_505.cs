public static BATBlock CreateEmptyBATBlock(POIFSBigBlockSize bigBlockSize, bool isXBAT){
    BATBlock block = new BATBlock(bigBlockSize);
    if (isXBAT){
        block._values[0] = POIFSConstants.END_OF_CHAIN;
    }
    else{
        block._values[1] = POIFSConstants.END_OF_CHAIN;
    }
    return block;
}