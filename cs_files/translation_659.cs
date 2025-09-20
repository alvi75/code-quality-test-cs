public override char Get(int index){
    CheckIndex(index);
    return sequence[index];
}
else{
    throw new IndexOutOfRangeException("Unable to fetch character at index " + index + ".");
}
}