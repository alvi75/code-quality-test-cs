public virtual E pollFirst(){
    return (_size == 0) ? default(E) : removeFirstImpl();
}