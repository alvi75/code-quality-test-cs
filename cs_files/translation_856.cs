public virtual void Swap(){
    int sBegin = beginA;
    int sEnd = endA;
    beginA = beginB;
    endA = endB;
    beginB = sBegin;
    endB = sEnd;
}