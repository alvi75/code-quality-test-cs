public virtual OpenStringBuilder Append(string csAppendable appendable){
    if (appendable == null){
        throw new System.ArgumentNullException("appendable", "value cannot be null");
    }
    lock (@lock){
        expand(appendable.Length);
        appendable.write(buf, 0, appendable.Length);
        return this;
    }
}