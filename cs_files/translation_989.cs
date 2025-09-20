public bool Find(int start){
    findPos = start;
    if (findPos < regionStart){
        findPos = regionStart;
    }
    else{
        if (findPos >= regionEnd){
            matchFound = false;
            return false;
        }
    }
}
matchFound = FindImpl(address, input, findPos, match);
if (matchFound){
    findPos = match[1];
}
return matchFound;
}