public static int GetUniqueAlt(IEnumerable<BitSet> altsets){
    BitSet all = GetAlts(altsets);
    if (all.Cardinality() == 1){
        return all.NextSetBit(0);
    }
    else{
        return Atn.ATN.INVALID_ALT_NUMBER;
    }
}