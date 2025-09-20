public override string ToString(){
    StringBuilder b = new StringBuilder();
    int length_1 = Length;
    b.Append(GetFileSeparatorChar());
    for (int i = 0;
    i < length_1;
    i++){
        b.Append(GetComponent(i));
        if (i < length_1 - 1){
            b.Append(GetFileSeparatorChar());
        }
    }