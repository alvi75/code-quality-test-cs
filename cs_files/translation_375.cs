override public java.util.List<E> subList(int start, int end){
    lock (mutex){
        return new java.util.Collections.SynchronizedList<E>(list.subList(start, end), mutex);
    }
}