public virtual bool CanAppend(){
    foreach (Head head in heads){
        if (head != LastHead.instance){
            return true;
        }
    }
    appendable = new StringBuilder();
}
return false;
}