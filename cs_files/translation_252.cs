public virtual E pollLast(){
    java.util.MapClass.Entry<E, object> entry = backingMap.pollLastEntry();
    return (entry == null) ? default(E) : entry.getKey();
}