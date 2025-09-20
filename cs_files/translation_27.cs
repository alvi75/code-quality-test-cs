public override bool Equals(object o){
    var other = o as FacetLabel;
    if (other == null){
        return false;
    }
    if (_Length != other._length){
        return false;
    }
    for (int i = _length - 1;
    i >= 0;
    i--){
        if (!_Components[i].Equals(other._components[i])){
            return false;
        }
    }
    return true;
}