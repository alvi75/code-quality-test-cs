public NGit.Diff.Edit After(NGit.Diff.Edit cut){
    return new NGit.Diff.Edit(beginA + cut.beginA, cut.beginA, beginB + cut.beginB, cut.endB);
}