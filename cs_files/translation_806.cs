public sealed override byte get(){
    if (_position == _limit){
        throw new java.nio.BufferUnderflowException();
    }
    return backingArray[offset + _position++];
}