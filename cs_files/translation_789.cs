public bool LessThan(TextFragment fragA, TextFragment fragB){
    if (fragA.Score == fragB.Score){
        return fragA.FragNumber > fragB.FragNumber;
    }
    else{
        return fragA.Score < fragB.Score;
    }
}