public virtual java.util.Iterator<E> iterator(){
    object[] snapshot = elements;
    return new java.util.concurrent.CopyOnWriteArrayList.CowIterator<E>(snapshot, 0,snapshot.Length);
}