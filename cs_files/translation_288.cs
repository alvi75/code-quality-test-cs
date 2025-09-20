public override bool Equals(object o){
    if (o == this){
        return true;
    }
    if (!(o is java.util.Set<E>)){
        return false;
    }
    java.util.Set<E> s = (java.util.Set<E>)o;
    try{
        return _size == s.size() && java.util.Collections.addAll(_elements, s));
    }
    catch (System.ArgumentException){
        return false;
    }
    catch (System.NullReferenceException){
        return false;
    }
}