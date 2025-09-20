public void SetPrecedenceSuppressed(bool value){
    if (value){
        this.reachesIntoOuterContext |= 0x40000000;
    }
    else{
        this.reachesIntoOuterContext &= ~SUPPRESS_PRECEDENCE_FILTER;
    }
}